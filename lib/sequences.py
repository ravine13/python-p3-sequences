#!/usr/bin/env python3


def print_fibonacci(length=None):
    fibonacci_list = []

    if length == 0:
        print ([])
    elif length == 1:
        print('[0]')
    else:
        fibonacci_list = [0, 1]
        if length > 2:
            i = 2
            while i < length:
                value = fibonacci_list[i - 1] + fibonacci_list[i - 2]
                fibonacci_list.append(value)
                i += 1

        print(fibonacci_list)
