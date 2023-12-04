# python -m doctest -v calculadora.py - to see the results of the doctest


def soma(x, y):  # type: ignore
    """Soma x e y

    >>> soma(10, 20)
    31
    """
    return x + y  # type: ignore
    # assert isinstance(x, (int, float)), "x precisa ser int ou float!"
    # assert isinstance(y, (int, float)), "y precisa ser int ou float!"


if __name__ == "__name__":
    import doctest

    doctest.testmod(verbose=True)
# verbose = True is not showing the details of the doctest
