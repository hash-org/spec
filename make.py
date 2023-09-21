#!/usr/bin/env python
"""
This script is used to build the documentation for the project. It is
responsible for creating the virtual environment, installing the
dependencies, and then invoking the sphinx build process.
"""

import argparse
import subprocess
import os
import sys
import venv
from pathlib import Path
from typing import Optional, Literal


class VirtualEnv:
    path: Path
    requirements: Path
    installed_requirements: Path

    def __init__(self, root: Path, path: Path):
        self.path = path
        self.requirements = root / "requirements.txt"
        self.installed_requirements = path / "installed-requirements.txt"

        if not self.up_to_date():
            self.create()

    def bin(self, name: str) -> Path:
        """
        Get a path to the particular executable/binary/library in the environment.
        """
        if sys.platform == "win32":
            return self.path / "scripts" / name
        else:
            return self.path / "bin" / name

    def up_to_date(self) -> bool:
        """
        Check whether the current requirements are up-to-date with the installed
        requirements. If they are not, then this will return False.
        """
        if self.installed_requirements.exists():
            expected = self.requirements.read_bytes()
            installed = self.installed_requirements.read_bytes()

            if expected == installed:
                return True
        return False

    def create(self):
        """
        Create the VirtualEnv and install all the required dependencies.
        """

        venv.EnvBuilder(clear=True, symlinks=True, with_pip=True).create(self.path)
        subprocess.run(
            [self.bin("pip"), "install", "-r", self.requirements, "--require-hashes"],
            check=True,
        )

        self.installed_requirements.write_bytes(self.requirements.read_bytes())


def current_git_commit(root: Path) -> Optional[str]:
    """
    Attempt to extract the current git commit hash from the
    repository.
    """
    try:
        return (
            subprocess.run(
                ["git", "rev-parse", "HEAD"],
                check=True,
                stdout=subprocess.PIPE,
            )
            .stdout.decode("utf-8")
            .strip()
        )
    # `git` executable missing from the system
    except FileNotFoundError:
        print("warning: failed to detect git commit: missing executable git")
        return
    # `git` returned an error (git will print the actual error to stderr)
    except subprocess.CalledProcessError:
        print("warning: failed to detect git commit: git returned an error")
        return


def build_docs(
    root: Path,
    env: VirtualEnv,
    builder: Literal["html"],
    clear: bool,
    serve: bool,
    debug: bool,
):
    """
    Function which invokes the actual build process with the desired arguments.

    :param root: The root of the project
    :param env: The virtual environment to use (used to resolve where the binaries to sphinx are).
    :param builder: The builder to use (html, pdf, etc.)
    :param clear: Whether to clear the pre-built sources
    :param serve: Whether to serve the docs immediately, and just reload when we notice changes.
    :param debug: Whether to enable debug mode for the extensions, showing exceptions. This mode
                  is mutually exclusive with `serve`.
    """
    dest = root / "build"
    args = ["-b", builder, "-d", dest / "docs"]

    if debug:
        # Disable parallel builds and show exceptions in debug mode.
        #
        # `-j 1` - sets the job count to 1
        # `-T`   - show full traceback on exception
        args += ["-j", "1", "-T"]
    else:
        # Enable parallel builds
        args += ["-j", "auto"]

    # If we want to clear the pre-built sources...
    if clear:
        args.append("-E")

    # If we want to serve the docs immediately, and just reload
    # when we notice changes.
    if serve:
        args += ["--watch", root / "extensions", "--watch", root / "themes"]
    else:
        args += ["-W", "--keep-going"]

    # Add to build information about the commit version, and bake it
    # into the documentation that we are building.
    commit = current_git_commit(root)
    if commit is not None:
        args += ["-D", f"html_theme_options.commit={commit}"]

    # Finally try to run the application
    try:
        subprocess.run(
            [
                env.bin("sphinx-autobuild" if serve else "sphinx-build"),
                *args,
                root / "src",
                dest / builder,
            ],
            check=True,
        )
    except KeyboardInterrupt:
        # The user has told us to stop...
        exit(1)
    except subprocess.CalledProcessError:
        # something went wrong with building the actual spec.
        print("\nif an exception was thrown, run with `--debug` for full stack trace")
        exit(1)

    return dest / builder


def main(root: str):
    root = Path(root)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--clear", help="disable incremental builds", action="store_true"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-s",
        "--serve",
        help="start a local server with live reload",
        action="store_true",
    )

    group.add_argument(
        "--debug",
        help="Debug mode for the extensions, showing exceptions",
        action="store_true",
    )
    args = parser.parse_args()
    env = VirtualEnv(root, root / ".venv")

    # @@Todo: add pdf pipeline here...
    build_docs(root, env, "html", args.clear, args.serve, args.debug)


if __name__ == "__main__":
    main(os.path.abspath(os.path.dirname(__file__)))
