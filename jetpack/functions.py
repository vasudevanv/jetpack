import functools


def first(x):
    return x[0]


def last(x):
    return x[-1]


def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)




