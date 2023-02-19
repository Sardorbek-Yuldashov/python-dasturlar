def map(func,iterable):
    s = []
    for i in iterable:
        s.append(func(i))
    return s
print(map(lambda x: x // 2, [1, 2, 3, 4]))