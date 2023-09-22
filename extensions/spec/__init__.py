from typing import Iterable, Optional, Dict

from sphinx.application import Sphinx
from sphinx.domains import Domain

from . import definitions, pages
from . import syntax_directive


class SpecDomain(Domain):
    name = "spec"
    label = "Specification"
    roles = {**definitions.get_roles()}
    directives = {
        "syntax": syntax_directive.SyntaxDirective,
        "informational-page": pages.build_information_directive("page"),
        "informational-section": pages.build_information_directive("section"),
    }
    object_types = definitions.get_object_types()
    indices = []

    def get_objects(self) -> Iterable[tuple[str, str, str, str, str, int]]:
        return definitions.get_objects(self.env)

    def merge_domaindata(self, docnames: list[str], otherdata: dict):
        def is_empty(data: Optional[Dict[str, str]]) -> bool:
            return not data or list(data.keys()) == ["version"]

        if not is_empty(self.data) or not is_empty(otherdata):
            raise NotImplementedError(
                "data in the domain, `merge_domaindata()` should be implemented"
            )


def setup(app: Sphinx):
    """
    Setup the `spec` extension in the application. This will add:

    - The `spec` domain
    - The `spec` directives
    - The `spec` roles
    """
    app.add_domain(SpecDomain)
    definitions.setup(app)
    pages.setup(app)

    return {
        "version": "0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
