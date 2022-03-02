import doctest

EPSILON = 0.0001

def find_root(func, lower, upper):
    #Examples
    """
    >>> find_root(lambda x: x**2 - 4, 1, 3)
    2.0
    
    >>> f = lambda x: x ** 2 - 81
    >>> find_root(f, 5, 10)
    9.0

    >>> f = lambda x: x ** 3 - 1
    >>> find_root(f, 0, 2)
    1.0
    """
    iterations=100 #number of iteration
    xn = lower
    range = upper - lower
    while lower <= upper:
        lower += range / iterations #length of each iteration
        xn_value = func(xn)
        if abs(xn_value) < EPSILON: # found solution with accuracy of epsilon
            return float("{:.4f}".format(xn))
        derivative = (func(xn + EPSILON) - func(xn)) / EPSILON  #f'(x) = f(x+h)-f(x)]/h
        #calculation according to derivative definition
        if derivative == 0:
            return None #no solution
        xn = xn - xn_value / derivative  #next xn according to Newton-Rapson
    return None #no solution

if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
