#!/usr/bin/env python3


def print_fibonacci(length):
    fibonacci_list = []

    if length > 0:
        fibonacci_list.append(0)
        if length > 1:
            fibonacci_list.append(1)
            if length > 2:
                i = 2
                while i < length:
                    value = fibonacci_list[i-1] + fibonacci_list[i-2]
                    fibonacci_list.append(value)
                    i += 1

    print(fibonacci_list)