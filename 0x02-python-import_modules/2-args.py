#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv) - 1

    if x == 0:
        print("{:d} arguments.".format(x))
    elif x == 1:
        print("{:d} argument:".format(x))
    else:
        print("{:d} arguments:".format(x))

    if x >= 1:
        x = 0
        for arg in sys.argv:
            if x != 0:
                print("{:d}: {}".format(x, arg))
            x += 1
