from typing import Sequence, Generator, Optional, List
from enum import Enum

from docutils import nodes
from docutils.nodes import Node
from sphinx.util.docutils import SphinxDirective

from . import definitions


class SyntaxDirective(SphinxDirective):
    has_content = True

    def run(self) -> Sequence[Node]:
        # This to avoid a weird issue in Sphinx which randomly invokes the Sphinx
        # syntax highlighting to fire on syntax blocks that have special formatting
        # on them.
        #
        # The reason why Sphinx does this is it checks if the "raw source" of the
        # node is compared to the `astext()` of the node. Since for this node, we don't
        # really care about the raw source, we set the raw source something that will
        # never appear in `astext()`, thus turning off the syntax highlighting.
        node = nodes.literal_block("\0")

        # Add the CSS class to the node
        node["classes"].append("spec-syntax")

        # Parse and create the actual content of the
        # syntax
        for child in Parser("\n".join(self.content), self.env.docname).parse():
            node += child

        return [node]


class TokenKind(Enum):
    """
    The kind of token that can appear within the syntax block.
    """

    # identifier, `name`
    IDENT = 1

    # `::=`
    DEF = 2

    # A literal, `$$1$$`
    LIT = 3

    # Some kind of whitespace.
    WHITESPACE = 4

    # some other token
    OTHER = 5


class Token:
    kind: TokenKind
    content: str

    def __init__(self, kind: TokenKind, content: str):
        self.kind = kind
        self.content = content


class Lexer:
    pos: int = 0
    content: str = ""

    def __init__(self, content: str):
        self.pos = 0
        self.content = content

    def lex(self) -> Generator[Token, None, None]:
        """
        Lex the next token from the input stream.
        """
        while True:
            char = self.next()
            if char is None:
                return

            if char == "$" and self.peek() == "$":
                self.next()  # eat `$`

                buf = ""
                while True:
                    peeked = self.peek()
                    if peeked is None:
                        return

                    # Handle the case of `$$$$$`
                    elif peeked == "$" and self.peek(1) == "$" and self.peek(2) != "$":
                        self.next()  # eat the `$`
                        self.next()  # eat the `$`
                        break
                    else:
                        buf += self.next()
                yield Token(TokenKind.LIT, buf)

            elif char == ":" and self.peek() == ":" and self.peek(1) == "=":
                self.next()  # eat the `:`
                self.next()  # eat the `=`
                yield Token(TokenKind.DEF, "::=")

            elif char.isalpha():
                buf = char
                while True:
                    peeked = self.peek()
                    if peeked is None or not (peeked.isalpha() or peeked == "_"):
                        break
                    buf += self.next()
                yield Token(TokenKind.IDENT, buf)
            elif char.isspace():
                buf = char
                while True:
                    peeked = self.peek()
                    if peeked is None or not peeked.isspace():
                        break
                    buf += self.next()
                yield Token(TokenKind.WHITESPACE, buf)
            else:
                yield Token(TokenKind.OTHER, char)

    def peek(self, nth: int = 0) -> Optional[str]:
        """
        Peek the `nth` character forwards.
        """
        try:
            return self.content[self.pos + nth]
        except IndexError:
            return None

    def next(self) -> Optional[str]:
        """
        Get the next character and increment the current position.
        """
        try:
            char = self.content[self.pos]
        except IndexError:
            return None

        self.pos += 1
        return char


class Parser:
    content: str
    document_name: str
    peek_buf: List[Token]
    lexer: Generator[Token, None, None]

    def __init__(self, content: str, document_name: str):
        self.content = content
        self.document_name = document_name
        self.lexer = Lexer(content).lex()
        self.peek_buf = []

    def parse(self) -> Generator[Node, None, None]:
        """
        This will parse the syntax block and generate nodes with the
        appropriate styling.
        """

        while True:
            token = self.next()
            if token is None:
                break

            match token.kind:
                case TokenKind.LIT:
                    node = nodes.strong("", token.content)
                    node["classes"].append("spec-syntax-literal")
                    yield node

                case TokenKind.IDENT:
                    if not Parser.is_syntax_ident(token.content):
                        yield nodes.Text(token.content)

                    if self.peek_kind(
                        TokenKind.DEF, int(self.peek_kind(TokenKind.WHITESPACE))
                    ):
                        yield definitions.DefId("syntaxes", token.content)
                    else:
                        yield definitions.DefRef(
                            "syntaxes", self.document_name, token.content
                        )
                case _:
                    yield nodes.Text(token.content)

    def next(self) -> Optional[Token]:
        """
        Get the next token from the lexer.
        """

        if self.peek_buf:
            return self.peek_buf.pop(0)
        else:
            return next(self.lexer, None)

    def peek_kind(self, kind: TokenKind, nth: int = 0) -> bool:
        """
        Check if the `nth` token is of the given kind.
        """
        peeked = self.peek(nth)
        return peeked is not None and peeked.kind == kind

    def peek(self, nth: int = 0) -> Optional[Token]:
        """
        Peek the `nth` token forwards.
        """

        while len(self.peek_buf) <= nth:
            token = next(self.lexer, None)
            if token is None:
                return None

            self.peek_buf.append(token)

        return self.peek_buf[nth]

    @staticmethod
    def is_syntax_ident(ident: Optional[str]) -> bool:
        """
        Ensures that the given identifier is of the expected format.

        N.B. this doesn't do anything since we don't have any specific rules for identifier
        names.
        """

        # @@Todo: decide on the rules about what we want to do here...
        return True
