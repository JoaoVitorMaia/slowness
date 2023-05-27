from frontend.Parser import Parser as p
import json


def repl():
    print("REPL v0.1")
    Parser = p()
    while True:
        prompt = input("> ")
        program = Parser.produceAST(prompt)
        print(json.dumps(program.__dict__, default=lambda o: o.__dict__, indent=4))


repl()
