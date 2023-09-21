import gc
from typing import List, Optional, Tuple

from docutils import nodes
from docutils.nodes import Node
from sphinx import addnodes
from sphinx.directives.other import TocTree
from sphinx.environment import BuildEnvironment
from sphinx.environment.collectors.toctree import TocTreeCollector


class AppendicesDirective(TocTree):
    """
    A wrapper directive around a toctree directive that indicates that the toctree
    contains appendices.
    """

    def run(self) -> List[Node]:
        result = super().run()

        # We modify the result of Sphinx's builtin toctree directive, so
        # ensure that it contains what we expect.
        AppendicesDirective.compatability_check(isinstance(result, list))
        AppendicesDirective.compatability_check(len(result) == 1)
        AppendicesDirective.compatability_check(isinstance(result[0], nodes.compound))
        AppendicesDirective.compatability_check(len(result[0].children) == 1)
        AppendicesDirective.compatability_check(
            isinstance(result[0].children[0], addnodes.toctree)
        )

        # Mark the toctree as containing appendices, so that the environment collector
        # can distinguish between the two.
        result[0].children[0]["appendices"] = True
        return result

    @staticmethod
    def compatability_check(condition: bool):
        """
        Test a condition, if false then emit a runtime error specifying that the
        builtin toctree builder has changed and this extension needs to be updated.
        """
        if not condition:
            raise RuntimeError(
                "the `toctree` Sphinx directive used by appendices emitted unexpected nodes"
                ", fix me so I can handle them!"
            )


class TocTreeCollectorWithAppendices(TocTreeCollector):
    __with_appendices: bool = False
    __chapter_offset: int = 0
    __chapter_max: int = 0
    __appendix_offset: int = 0
    __appendix_max: int = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def assign_section_numbers(self, env: BuildEnvironment) -> list[str]:
        """
        Assign a section number to each heading under a numbered toctree.

        Additionally, we will replace the `totree` if we see that there is an
        `appendices` directive in the toctree.
        """
        result = super().assign_section_numbers(env)

        for doc_name in env.numbered_toctrees:
            doc_tree = env.get_doctree(doc_name)
            for toc_tree in doc_tree.findall(addnodes.toctree):
                self.__replace_toc_tree(env, toc_tree)

                self.__chapter_offset = self.__chapter_max
                self.__appendix_offset = self.__appendix_max

        return result

    def __replace_toc_tree(self, env: BuildEnvironment, toctree: Node):
        """
        Replace the section numbers in the toc tree. This will check whether
        the toctree contains an `appendices` directive, and if it does, then
        it will use the appendix numbering system for all items after the
        `appendices` directive.
        """

        # Now we have reached the appendices, we now use the Appendix numbering
        # system.
        self.__with_appendices = "appendices" in toctree

        # loop over all the entries in the tree and appropriately re-number them
        # and replace any nested toc trees.
        for _, ref in toctree["entries"]:
            env.titles[ref]["secnumber"] = self.__re_number(
                env.titles[ref]["secnumber"]
            )

            if ref in env.tocs:
                self.__replace_toc(env, ref, env.tocs[ref])

    def __replace_toc(self, env: BuildEnvironment, ref: Node, toc: Node):
        """
        Replace the section numbers in the toc tree.
        """

        if isinstance(toc, nodes.reference):
            fixed_number = self.__re_number(toc["secnumber"])
            toc["secnumber"] = fixed_number
            env.toc_secnumbers[ref][toc["anchorname"]] = fixed_number

        elif isinstance(toc, addnodes.toctree):
            raise RuntimeError("nested toc trees are not supported")
        else:
            for child in toc.children:
                self.__replace_toc(env, ref, child)

    def __re_number(self, number: Optional[Tuple[int, str]]) -> Tuple[int, str]:
        """
        Re-number the section number, this will increment the chapter or appendix
        number as appropriate.
        """

        if not number:
            return number

        if self.__with_appendices:
            with_offset = self.__appendix_offset + number[0]
            if with_offset > 26:
                # @@Improve: we could support more than 26 appendices by using
                #            a different numbering scheme.
                raise RuntimeError("too many appendices!")

            fixed = chr(ord("A") - 1 + with_offset)
            self.__appendix_max = max(self.__appendix_max, with_offset)
        else:
            fixed = self.__chapter_offset + number[0]
            self.__chapter_max = max(self.__chapter_max, fixed)

        return fixed, *number[1:]


def disable_builtin_toctree(app):
    """
    Function to disable the builtin toctree collector, we do this by finding the
    collector and invoking `disable()` on it.

    This is need to avoid two TocTreeCollectors running at the same time in the
    application.
    """
    for obj in gc.get_objects():
        if isinstance(obj, TocTreeCollector):
            obj.disable(app)


def setup(app):
    app.add_directive("appendices", AppendicesDirective)

    # @@Hack: we just yeet the builtin toctree collector via gc!
    disable_builtin_toctree(app)
    app.add_env_collector(TocTreeCollectorWithAppendices)

    return {
        "version": "0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
