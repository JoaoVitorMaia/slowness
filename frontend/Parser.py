from frontend.AST import Statement, Expression, NumericLiteral, Identifier, BinaryExpression, Program
from frontend.lexer import tokenize, Token, TokenType
import json


class Parser:
    def __init__(self) -> None:
        self.tokens = []

    def not_eof(self):
        return self.tokens[0].type != TokenType.EOF

    def parse_statement(self):
        return self.parse_expression()

    def produceAST(self, sourceCode: str):
        self.tokens = tokenize(sourceCode)
        program = Program()
        while self.not_eof():
            program.body.append(self.parse_statement())
        return program

    def eat(self):
        return self.tokens.pop(0)

    def at(self):
        return self.tokens[0]

    def parse_expression(self) -> Expression:
        # return self.parse_primary_expression()
        return self.parse_additive_expression()

    def parse_additive_expression(self) -> Expression:
        left = self.parse_multiplicative_expression()
        while self.at().value == "+" or self.at().value == "-":
            operator = self.eat().value
            right = self.parse_multiplicative_expression()
            left = BinaryExpression(left=left, right=right, operator=operator)
        return left

    def parse_multiplicative_expression(self) -> Expression:
        left = self.parse_primary_expression()
        while self.at().value == "/" or self.at().value == "*" or self.at().value == "%":
            operator = self.eat().value
            right = self.parse_primary_expression()
            left = BinaryExpression(left=left, right=right, operator=operator)
        return left

    # Ordem de prescedencia
    # AssignmentExpr
    # MemberExpr
    # FunctionCall
    # LogicalExpr
    # AdditiveExpr
    # MultiplicativeExpr
    # UnaryExpr
    # PrimaryExpr
    # ComparisonExpr
    def parse_primary_expression(self) -> Expression:
        tokenType = self.at().type
        if tokenType == TokenType.Identifier:
            return Identifier(self.eat().value)
        if tokenType == TokenType.Number:
            return NumericLiteral(float(self.eat().value))
        if tokenType == TokenType.OpenParen:
            self.eat()  # come o primeiro parenteses
            value = self.parse_expression()
            # come o ultimo parenteses
            self.expect(TokenType.CloseParen,
                        "Unexpected token found inside parenthesised expression. Expecting closing parenthesis")
            return value
        print(f"Unexpected token type {tokenType}")
        exit(1)

    def parse_statement(self) -> Statement:
        # um dia vai ter statamentes pra parserar
        return self.parse_expression()

    def expect(self, type: TokenType, err_msg: str):
        prev = self.eat()
        if not prev or prev.type != type:
            print(f'Parser error:\n{err_msg},{prev} - Expecting {type}')
