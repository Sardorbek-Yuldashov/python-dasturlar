def map_square(iterable):
    return map(lambda x: x**2, iterable)
print(list(map_square([1, 2, 3, 4])))
print(list(map_square((1, 2, 3, 4))))
print(type(map_square([1, 2, 3, 4])))