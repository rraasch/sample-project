#!/usr/bin/env python

from add import add_stuff, multiply_stuff
import click

def use_funcs(x, y):
    return add_stuff(x, y)


if __name__ == "__main__":
    x = 1
    y = 2
    print(use_funcs(x, y))
