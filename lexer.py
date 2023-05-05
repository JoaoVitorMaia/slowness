from enum import Enum
import sys,time

class TokenType(Enum):
    Number=1
    Identifier=2
    Equals=3
    OpenParen=4
    CloseParen=5
    BinaryOperator=6
    Hash=7
    Set=8
    Evaluate=9
    If = 10
    Elseif = 11
    Else = 12
    End = 13
    Foreach = 14
    In = 15
    Parse = 16
    Include = 17
    Macro = 18
    Stop = 19
    Break = 20
    Define = 21
    DolarSign = 22
    Dot = 23
    Quote = 24
    Less = 25
    Greater = 26
    NegationMark = 27
    EOF = 28

KEYWORDS = {
    'if': TokenType.If,
    'elseif': TokenType.Elseif,
    'else': TokenType.Else,
    'end': TokenType.End,
    'foreach': TokenType.Foreach,
    'in': TokenType.In,
    'set': TokenType.Set,
    'parse': TokenType.Parse,
    'include': TokenType.Include,
    'macro': TokenType.Macro,
    'stop': TokenType.Stop,
    'break': TokenType.Break,
    'define': TokenType.Define,
    'evaluate': TokenType.Evaluate,
}

class Token:
    def __init__(self, value:str, type: TokenType):
        self.value = value
        self.type = type

def isskipable(user_string:str):
    return user_string == ' ' or user_string == '\n' or user_string == '\t'

def iscomparisonoperator(user_string: str):
    return user_string == '<' or user_string == '>' or user_string == '!' or user_string == '='

def tokenize(source:str):
    tokens = []
    src = list(source)
    #construir cada token até o fim do arquivo
    while len(src) > 0:
        if src[0] == '(':
            tokens.append(Token(src.pop(0), TokenType.OpenParen))
        elif src[0] == ')':
            tokens.append(Token(src.pop(0), TokenType.CloseParen))
        elif src[0] == '*' or src[0] == '+' or src[0] == '-' or src[0] == '/' or src[0] == '%' or src[0] == '<' or src[0] == ">" or src[0] == "!" or src[0] == "&" or src[0] == '|':
            tokens.append(Token(src.pop(0), TokenType.BinaryOperator))
        elif src[0] == '=':
            tokens.append(Token(src.pop(0), TokenType.Equals))
        elif src[0] == '#':
            tokens.append(Token(src.pop(0), TokenType.Hash))
        elif src[0] == '$':
            tokens.append(Token(src.pop(0), TokenType.DolarSign))
        elif src[0] == '.':
            tokens.append(Token(src.pop(0), TokenType.Dot))
        elif src[0] == '"' or src[0] == '"':
            tokens.append(Token(src.pop(0), TokenType.Quote))
        elif src[0] == '!':
            tokens.append(Token(src.pop(0), TokenType.NegationMark))
        else:
            # Lidar com tokens multicaracteres
            if src[0].isdigit():
                num = ""
                while(len(src)>0 and src[0].isdigit()):
                    num+=src.pop(0)
                tokens.append(Token(num, TokenType.Number))
            elif src[0].isalpha():
                ident=""
                while len(src) > 0 and (src[0].isalpha() or src[0].isdigit()):
                    ident+=src.pop(0)
                if ident not in KEYWORDS:
                    tokens.append(Token(ident, TokenType.Identifier))
                else:
                    tokens.append(Token(ident, KEYWORDS[ident]))

            elif isskipable(src[0]):
                src.pop(0)
            else:
                print(f'Unrecognized character {src[0]}')
                sys.exit()

        
    tokens.append(Token(value="", type=TokenType.EOF))
    return tokens

with open('tst.vm', 'r') as file:
    for token in tokenize(file.read()):
        print(token.__dict__)
