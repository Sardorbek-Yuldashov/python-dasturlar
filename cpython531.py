def filter_odd(iterable):
    return filter(lambda x: x%2==0, iterable)

print(list(filter_odd([1, 2, 3, 4])))
print(type(filter_odd([1, 2, 3, 4])))
