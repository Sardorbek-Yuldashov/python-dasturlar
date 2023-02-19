def map(func,itr):
    s = []
    for i in itr:
        s.append(func(i))
    return s
print(map(lambda x: x // 2, [1, 2, 3, 4]))