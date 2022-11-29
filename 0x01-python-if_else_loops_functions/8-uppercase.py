#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = ord(str[i])
        if (c >= 97 and c <= 122):
            c -= 32
        print(f'{chr(c)}', end="")
    print()
