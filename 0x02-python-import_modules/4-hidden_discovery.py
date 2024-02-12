#!/usr/bin/python3
import hidden_4


def main():
    # `dir()` finds out which names a module defines
    names = dir(hidden_4)
    for i in names:
        if not i.startswith("__"):
            print("{}".format(i))


if __name__ == "__main__":
    main()
