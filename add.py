def add_stuff(x: int, y: int):
    return int(x+y)

def multiply_stuff(*args):
    prod = 1
    for i in args:
        prod *= i
    return prod
