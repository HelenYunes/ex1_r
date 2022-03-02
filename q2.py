import doctest

def sort_helper(data):
    depth_check= True
    if type(data) is not list and type(data) is not tuple and type(data) is not dict and type(data) is not set:
        return data
    for v in data:
        if isinstance(v, list) or isinstance(v, tuple):
            depth_check=False
    if depth_check:
        return sorted(data)
    n_deep_arrang, deep_arrang  = [] ,[] 
    for v in data:
        if isinstance(v, list) or isinstance(v, tuple): #list/tuple case
            deep_arrang.append(sort_helper(v))
        else:
            n_deep_arrang.append(v)
    return sorted(n_deep_arrang) + sorted(deep_arrang, key=sum)


def print_sorted(data):
    #Examples
    """
    >>> print_sorted({"a": 5, "c": 6, "b": [1, 3, 2, 4]})
    {'a': 5, 'b': [1, 2, 3, 4], 'c': 6}
    
    >>> print_sorted([2, 1, 9, 0, [7, 6, 3, 8], 5, [6, 5], 4])
    [0, 1, 2, 4, 5, 9, [5, 6], [3, 6, 7, 8]]
    
    >>> print_sorted(('a', 'c', 'd', (5, 0, 10,2), 'b'))
    ('a', 'b', 'c', 'd', [0, 2, 5, 10])
    """
    if isinstance(data, list): #list case
        print(sort_helper(data))
        return
    elif isinstance(data, tuple): #tuple case
        print(tuple(sort_helper(data)))
        return
    elif isinstance(data, dict): #dict case
        for key, val in data.items():
            data[key] = sort_helper(val)
        print(dict(sorted(data.items())))
        return
    else:
        print(data)
        return

if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

