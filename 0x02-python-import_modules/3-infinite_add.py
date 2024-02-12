#!/usr/bin/python3
from sys import argv


def main():
    sum = 0
    length = len(argv)
    for i in range(1, length):
        sum += int(argv[i])
    print(sum)


if __name__ == "__main__":
    main()
