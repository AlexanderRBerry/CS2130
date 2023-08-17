def recursive_fib(n):
    """Return the nth fibonacci number.  Use recursion to calculate """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_fib(n - 1) + recursive_fib(n - 2)


def fast_fib(n):
    """Return the nth fibonacci number.  Use a loop to calculate.
    Start with the first two numbers and then repeatedly calculate the next number"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    lastNum = 0
    lastLastNum = 1
    for result in range(n):
        result = lastNum + lastLastNum
        lastLastNum = lastNum
        lastNum = result
    return result


def matrix_fib(n):
    mat = [[1, 1], [1, 0]]
    if n < 2:
        return n
    matrix_pow(mat, n - 1)
    return mat[0][0]

def matrix_pow(A, n):
    if n == 1:
        return
    copy = [[A[0][0], A[0][1]], [A[1][0], A[1][1]]]
    matrix_pow(A, n // 2)
    matrix_multiply(A, A)
    if n % 2 != 0:
        matrix_multiply(A, copy)

def matrix_multiply(A, B):
    w = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    x = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    z = A[1][0] * B[0][1] + A[1][1] * B[1][1]

    A[0][0] = w
    A[1][0] = x
    A[0][1] = y
    A[1][1] = z
