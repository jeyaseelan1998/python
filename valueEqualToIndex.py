# import re


def count(s):
    u = 0
    l = 0
    n = 0
    sp = 0
    for char in str(s):
        if char.isupper():
            u += 1
        elif char.islower():
            l += 1
        elif char.isnumeric():
            n += 1
        else:
            sp += 1
    return "{}\n{}\n{}\n{}".format(u, l, n, sp)


# print(count("#GeeKs01fOr@gEEks07"))
print(count("ep&Cvh,(v#w'u;AUlM*)fH_2XCJ@950UH?J}q1T}mL"))
