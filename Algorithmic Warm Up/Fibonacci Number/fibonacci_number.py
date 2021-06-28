# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    rv = 0
    last = 0
    current = 1
    for _ in range(n - 1):
        #2 =  0  +   1
        rv = last + current
        last = current
        current = rv

    return rv


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))




# print(fibonacci_number_naive(2))
# print(fibonacci_number_naive(3))
# print(fibonacci_number_naive(5)) #5
# print(fibonacci_number_naive(6)) #8
#
# print(fibonacci_number(5)) #5
# print(fibonacci_number(6)) #8
