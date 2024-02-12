#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

from sys import argv, exit


def main():
    length = len(argv)
    if length != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operator = {'+': add, '-': sub, '*': mul, '/': div}
    if argv[2] not in list(operator.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    print("{} {} {} = {}".format(a, argv[2], b, operator[argv[2]](a, b)))


if __name__ == "__main__":
    main()
