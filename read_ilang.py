import sys
from typing import TextIO

# You can get antlr4 via pip3 install antlr4-python3-runtime

from antlr4 import *
from rtlilLexer import rtlilLexer
from rtlilParser import rtlilParser


class FailFastLexer(rtlilLexer):
    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)

    def recover(self, re: RecognitionException):
        raise SystemExit("Failed parsing")


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = FailFastLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = rtlilParser(stream)
    modules = parser.file_().ms
    print("".join([str(m) for m in modules]))


if __name__ == '__main__':
    main(sys.argv)
