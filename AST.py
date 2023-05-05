#apenas para facilitar a compreensao do programa
class Statement:
    pass

class Program(Statement):
    def __init__(self):
        super().__init__()
        self.kind = "Program"# para facilitar a leitura
        self.body = []#lista de statements

class Expression(Statement):#para legibilidade
    pass

class BinaryExpression(Expression):
    def __init__(self, left:Expression, rigth: Expression, operator:str) -> None:
        self.left = left
        self.rigth = rigth
        self.operator = operator

class Identifier(Expression):
    def __init__(self, symbol:str) -> None:
        super().__init__()
        self.kind = "Identifier"
        self.symbol = symbol


class NumericLiteral(Expression):
    def __init__(self, value:str) -> None:
        super().__init__()
        self.kind = "Identifier"
        self.value = value