#!/usr/bin/python3
if __name__ == "__main__":
    l = len(argv)
    if l == 0:
        print('{:d} arguments.'.format(l))
    elif l == 1:
        print('{:d} argument:'.format(l))
        print('{:d}: {:s}'.format(argv))
    else:
        print('{:d} arguments:'.format(l))
        for i in range(l):
            print('{:d}: {:s}'.format(argv[i]))
