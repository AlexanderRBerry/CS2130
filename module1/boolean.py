def multiply(x, y):
    """
    Computes Boolean multiplication.
    :param x: value of the first Boolean variable
    :param y: value of the second Boolean variable
    :return: result of Boolean multiplication
    """
    return x * y


def add(x, y):
    """
    Computes Boolean addition.
    :param x: value of the first Boolean variable
    :param y: value of the second Boolean variable
    :return: result of Boolean addition
    """
    if x + y >= 1:
        return 1
    else:
        return 0


def complement(x):
    """
    Computes Boolean complement.
    :param x: value of the Boolean variable
    :return: result of Boolean complement
    """
    if x == 1:
        return 0
    else:
        return 1


def expression1(x, y, z):
    """
    Computes the result of Boolean expression 1 specified in the instructions.
    :param x: value of the first Boolean variable
    :param y: value of the second Boolean variable
    :param z: value of the third Boolean variable
    :return: result of the Boolean expression
    """
    a = multiply(y, z)
    b = multiply(y, add(x, z))
    return add(a, b)


def expression2(x, y, z):
    """
    Computes the result of Boolean expression 2 specified in the instructions.
    :param x: value of the first Boolean variable
    :param y: value of the second Boolean variable
    :param z: value of the third Boolean variable
    :return: result of the Boolean expression
    """
    a = multiply(x, complement(y))
    b = add(x, complement(z))
    return add(a, b)


def expression3(x, y, z):
    """
    Computes the result of Boolean expression 3 specified in the instructions.
    :param x: value of the first Boolean variable
    :param y: value of the second Boolean variable
    :param z: value of the third Boolean variable
    :return: result of the Boolean expression
    """
    a = multiply(add(complement(x), y), complement(add(y, z)))
    b = multiply(multiply(complement(x), y), z)

    return add(a, b)
