def map_divisors_count(mp):
    def s(x):
        y = 0
        if x == 1:
            return 1
        if x <= 0:
            return 0
        for i in range(1, x + 1):
            if x % i == 0:
                y += 1
        return y

    return map(s, mp)


print(list(map_divisors_count([10, 2, 3, 0, -1, 4, 6, 1])))