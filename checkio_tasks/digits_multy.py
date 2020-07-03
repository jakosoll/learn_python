from functools import reduce

def checkio(number: int) -> int:
    result = 1
    for i in str(number):
        if int(i) != 0:
            result *= int(i)
    return result


def checkio_reduce(number: int) -> int:
    return reduce(lambda res, cur: res * (1 if cur == '0' else int(cur)), str(number), 1)


if __name__ == '__main__':
    print('Example:')
    print(checkio_reduce(123405))
    
