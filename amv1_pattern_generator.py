def pattern_generator(x, y, added):
    import random
    outer, inner = [],[]

    if added:
        for countRow in range(x):
            for countColumn in range(y):
                inner.append(0)
            outer.append(inner)
            inner = []

        return outer

    else:
        for countRow in range(x):
            for countColumn in range(int(y / 2)):
                inner.append(random.randint(0, 1))
            if y % 2 != 0:
                inner.append(random.randint(0, 1))
                inner.extend(inner[-2::-1])
            else:
                inner.extend(inner[-1::-1])
            outer.append(inner)
            inner = []

        return outer

