def map_divisors_count(iterable):
    def func(iterable2):
        y = 0
        if iterable2 == 1:
            return 1
        if iterable2 <= 0:
            return 0
        for i in range(1, iterable2 + 1):
            if iterable2 % i == 0:
                y += 1
        return y

    return map(func, iterable)


print(list(map_divisors_count([10, 2, 3, 0, -1, 4, 6, 1])))