def sum(first: int, second: int) -> int:
    return first + second


def minus(first: int, second: int) -> int:
    return first + second


def printMinusAndPlus(first: int, second: int) -> int:
    print(minus(first, second) + " " + sum(first, second))


print(sum(5, 25))
print(minus(10, 20))
printMinusAndPlus(10, 15)
