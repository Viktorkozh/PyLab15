#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def tag_decorator(tag):
    def decorator(func):
        def wrapper(text):
            return f"<{tag}>{func(text)}</{tag}>"
        return wrapper
    return decorator


@tag_decorator(tag="div")
def to_lowercase(input_string):
    return input_string.lower()


if __name__ == '__main__':
    print(to_lowercase(input("Введите слово для обертки: ")))
