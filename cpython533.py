def filter(func, iterable):
    s = []
    for i in iterable:
        if func(i):
            s.append(i)
    return s


print(filter(lambda x: x % 2 == 1, [1, 2, 3, 4]))