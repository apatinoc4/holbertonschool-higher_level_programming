#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argument = len(argv) - 1
    if argument == 1:
        print("{} argument:".format(argument))
    elif argument > 1:
        print("{} arguments:".format(argument))
    elif argument == 0:
        print("{} arguments.".format(argument))
    for i in range(argument):
        if argument != 0:
            print('{:d}: {:s}'.format(i + 1, argv[i + 1]))
