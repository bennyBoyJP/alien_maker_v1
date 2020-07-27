def pattern_generator(x, y, added):
    import random
    outer, inner = [],[]

    density = [0, 1, 0, 1, 0]

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
                inner.append(random.choice(density))
            if y % 2 != 0:
                inner.append(random.choice(density))
                inner.extend(inner[-2::-1])
            else:
                inner.extend(inner[-1::-1])
            outer.append(inner)
            inner = []

        return outer

