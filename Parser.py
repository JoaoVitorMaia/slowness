from AST import Statement, Expression, NumericLiteral, Identifier, BinaryExpression, Program
from lexer import tokenize, Token, TokenType


class Parser:
    def __init__(self) -> None:
        self.tokens = []
    def not_eof(self):
        return self.tokens[0] != TokenType.EOF
    def parse_statement(self):
        pass
    def produceAST(self, sourceCode:str):
        self.tokens = tokenize(sourceCode)
        program = Program()

        while self.not_eof():
            program.body.append(self.parse_statement())

