#!/usr/bin/python3
for i in range(0, 8):
    for j in range(0, 10):
        if i < j:
            print(f'{i}{j},', end=" ")
        else:
            continue
print(89)
