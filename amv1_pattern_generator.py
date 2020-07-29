def pattern_generator(x, y, added):
    import random
    outer, inner = [],[]

    randomDensity = random.randint(1, 10)
    if randomDensity < 3:
        density = [0, 0, 0, 1, 1]
    elif randomDensity < 10:
        density = [0, 0, 1, 1, 1]
    elif randomDensity == 10q



    qqq:
        density = [0, 0, 2, 2, 2]




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

