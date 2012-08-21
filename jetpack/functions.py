import functools

def first(x):
    return x[0]

def last(x):
    return x[-1]

def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def myround(x, base):
    """ Rounding values

    x: float
        Input value

    base: int
        Rounding basis
    """
    return base * round(x/base)