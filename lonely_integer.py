
n = int(input())
List = list(map(int, input().split()))


def lonelyInteger(list):
    val = 0
    for item in list:
        val = val ^ item
        print(val)
    return val

"""       val = val * item
item 0    val = 0 ^ 0 ---> val = 0
item 0    val = 0 ^ 0 ---> val = 0
item 1    val = 0 ^ 1 ---> val = 1
item 2    val = 1 ^ 2 ---> val = 3
item 1    val = 3 ^ 1 ---> val = 2
"""
print(lonelyInteger(List))
