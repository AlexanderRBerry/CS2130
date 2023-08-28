def is_one_to_one(domain, target, myRange):
    """
    Checks if a function has the one-to-one property.

    :param domain: A list of integers that define the domain of a function.
    :param target: A list of integers that define the target of a function.
    :param range: A list of integers that define the range of a function.
                  The domain and range must be in matching order. Each value in the
                  domain is expected to have a matching value in the range at the
                  same index that forms an ordered pair.
    :return: True if the function has the one-to-one property, False otherwise.
    """
    for r in range(len(myRange)):
        if myRange.count(myRange[r]) > 1:
            return False
    else:
        return True


def is_onto(domain, target, myRange):
    """
    Checks if a function has the onto property.

    :param domain: A list of integers that define the domain of a function.
    :param target: A list of integers that define the target of a function.
    :param range: A list of integers that define the range of a function.
                  The domain and range must be in matching order. Each value in the
                  domain is expected to have a matching value in the range at the
                  same index that forms an ordered pair.
    :return: True if the function has the onto property, False otherwise.
    """


def is_bijection(domain, target, range):
    """
    Checks if a function is a bijection.

    :param domain: A list of integers that define the domain of a function.
    :param target: A list of integers that define the target of a function.
    :param range: A list of integers that define the range of a function.
                  The domain and range must be in matching order. Each value in the
                  domain is expected to have a matching value in the range at the
                  same index that forms an ordered pair.
    :return: True if the function is a bijection, False otherwise.
    """

