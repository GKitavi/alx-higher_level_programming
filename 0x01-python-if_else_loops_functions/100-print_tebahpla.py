#!/usr/bin/python3
for i in range(0, 26):
    j = ord('z') - i
    if (i % 2 == 1):
        j = chr(j - ord('a') + ord('A'))
    else:
        j = chr(j)
    print("{}".format(j), end='')
