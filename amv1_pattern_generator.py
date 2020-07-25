def pattern_generator(x, y):
    import random
    outer, inner = [],[]

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
