#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    add = 0
    if length == 1:
        add = 0
    else:
        for bl in range(1, length):
            add += int(sys.argv[bl])
    print(add)
