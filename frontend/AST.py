import json
from enum import IntEnum
import pickle

# apenas para facilitar a compreensao do programa


class Statement:
    pass


class NodeType(IntEnum):
    Program = 1
    BinaryExpression = 2
    Identifier = 3
    NumericLiteral = 4


class Program(Statement):

    def __init__(self):
        super().__init__()
        self.kind = NodeType.Program  # para facilitar a leitura
        self.body = []  # lista de statements


class Expression(Statement):  # para legibilidade
    pass


class BinaryExpression(Expression):
    def __init__(self, left: Expression, right: Expression, operator: str) -> None:
        self.left = left
        self.right = right
        self.operator = operator
        self.kind = NodeType.BinaryExpression



class Identifier(Expression):
    def __init__(self, symbol: str) -> None:
        super().__init__()
        self.kind = NodeType.Identifier
        self.symbol = symbol



class NumericLiteral(Expression):
    def __init__(self, value: str) -> None:
        super().__init__()
        self.kind = NodeType.NumericLiteral
        self.value = value
