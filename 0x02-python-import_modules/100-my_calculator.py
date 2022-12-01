#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    l = len(sys.argv) - 1
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if l != 3:
        print(r'Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if l == 3:
        if sys.argv[2] == '+':
            print('{:d} {:c} {:d} = {:d}'.format(sys.argv[1], '+', sys.argv[3], add(a, b)))
        elif sys.argv[2] == '-':
            print('{:d} {:c} {:d} = {:d}'.format(sys.argv[1], '-', sys.argv[3], sub(a, b)))
        elif sys.argv[2] == '*':
            print('{:d} {:c} {:d} = {:d}'.format(sys.argv[1], '*', sys.argv[3], mul(a, b)))
        elif sys.argv[2] == '/':
            print('{:d} {:c} {:d} = {:d}'.format(sys.argv[1], '/', sys.argv[3], div(a, b)))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
