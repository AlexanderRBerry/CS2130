def conjunction(p, q):
    """
    Computes logical conjunction.
    :param p: value of the first logical variable
    :param q: value of the second logical variable
    :return: result of logical conjunction
    """
    if p == 'T' and q == 'T':
        return 'T'
    else:
        return 'F'

def disjunction(p, q):
    """
    Computes logical disjunction.
    :param p: value of the first logical variable
    :param q: value of the second logical variable
    :return: result of logical disjunction
    """
    if p == 'T' or q == 'T':
        return 'T'
    else:
        return 'F'

def negation(p):
    """
    Computes logical negation.
    :param p: value of the logical variable
    :return: result of logical negation
    """
    if p == 'T':
        return 'F'
    else:
        return 'T'

def conditional(p, q):
    """
    Computes logical conditional.
    :param p: value of the first logical variable
    :param q: value of the second logical variable
    :return: result of logical conditional
    """
    if p == 'T' and q == 'F':
        return 'F'
    else:
        return 'T'
def biconditional(p, q):
    """
    Computes logical biconditional.
    :param p: value of the first logical variable
    :param q: value of the second logical variable
    :return: result of logical biconditional
    """
    if p == 'T' and q == 'T':
        return 'T'
    elif p == 'F' and q == 'F':
        return 'T'
    else:
        return 'F'

def proposition1(p, q, r):
    """
    Computes the result of compound proposition 1 specified in the instructions.
    :param p: value of the first logical variable
    :param q: value of the second logical variable
    :param r: value of the third logical variable
    :return: result of the proposition
    """
    x = negation(conjunction(p, q))
    y = disjunction(r, q)
    return conjunction(x, y)

def proposition2(p, q, r):
    """
    Computes the result of compound proposition 2 specified in the instructions.
    :param p: value of the first logical variable
    :param q: value of the second logical variable
    :param r: value of the third logical variable
    :return: result of the proposition
    """
    x = conditional(q, r)
    y = conjunction(negation(p), r)
    return disjunction(x, y)

def proposition3(p, q, r):
    """
    Computes the result of compound proposition 3 specified in the instructions.
    :param p: value of the first logical variable
    :param q: value of the second logical variable
    :param r: value of the third logical variable
    :return: result of the proposition
    """
    x = conjunction(r, q)
    y = negation(disjunction(p, r))
    return biconditional(x, y)
