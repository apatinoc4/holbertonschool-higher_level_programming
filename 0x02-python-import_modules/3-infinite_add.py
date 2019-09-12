#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argument = len(argv)
    add = 0
    for i in range(argument):
        if i == 0:
            continue
        add += int(argv[i])
    print("{}".format(add))
