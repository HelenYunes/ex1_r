import doctest

def f(x: int, y: float, z):
    return x + y + z

def f2(course: str, year: str):
    return "Course: " + course + ", Year: " + year

def safe_call(f, **kwargs):
    #Examples
    """
    >>> safe_call(f, x=5, y=7.0, z=3)
    15.0
    >>> safe_call(f, x=0, y=7.0, z=3)
    10.0
    >>> safe_call(f, x=5, y=7.0, z=False)
    12.0
    >>> safe_call(f, x=5, y=7.0, z=False)
    12.0
    >>> safe_call(f2, course="Research algorithms",year="2022")
    'Course: Research algorithms, Year: 2022'
    """
    for index, val in kwargs.items():
        try:
            func_arg_type = f.__annotations__[index] #annotation in the given function
        except KeyError:
            continue
        if func_arg_type != type(val): #checks that the type of variables match
            raise TypeError(f"Argument {index} does not match {func_arg_type} type")
    return f(**kwargs)

if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

