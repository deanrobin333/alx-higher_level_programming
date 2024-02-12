#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

from sys import argv, exit


def main():
    length = len(argv)
    if length != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    operator = '+-*/'
    if operator.find(argv[2]) == -1:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        print("{} {} {} = {}".format(a, argv[2], b, add(a, b)))
    elif argv[2] == '-':
        print("{} {} {} = {}".format(a, argv[2], b, sub(a, b)))
    elif argv[2] == '*':
        print("{} {} {} = {}".format(a, argv[2], b, mul(a, b)))
    elif argv[2] == '/':
        print("{} {} {} = {}".format(a, argv[2], b, div(a, b)))


if __name__ == "__main__":
    main()
