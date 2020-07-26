def pattern_combiner(rows, columns, loops):

    from amv1_pattern_generator import pattern_generator

    def border_maker(y, inside):

        for item in inside:
            item.insert(0, 9)
            item.append(9)

        topBottomRow = [9 for iterations in range(y + 2)]

        inside.insert(0, topBottomRow)
        inside.append(topBottomRow)
        return inside

    def best_layout(number_of_patterns):

        addedPattern = False
        if number_of_patterns % 2 != 0:
            if (number_of_patterns ** .5) % 1 != 0:
                number_of_patterns += 1
                addedPattern = True

        a = number_of_patterns
        b = int((a / 2) - 1)
        difference = (0, 99 ** 99)
        for row in range(b, 0, -1):
            if a % row == 0:
                col = int(a / row)
                if abs(row - col) < difference[-1]:
                    difference = row, abs(row - col)
        c = difference[0]
        d = int(a / c)
        if c > d:
            c, d = d, c
        return c, d, addedPattern

    def pattern_display(patterns, axis1, axis2):

        currentRow = axis2
        patternsInRow = 0
        outer, inner = [], []

        while patternsInRow < axis1:
            axis2Counter = 0
            for rowsOfPattern in range(len(patterns[0])):
                for currentPattern in range((currentRow - axis2), currentRow):

                    if axis2Counter < axis2:
                        print(f'currentPattern:{currentPattern} rowsOfPattern:{rowsOfPattern}')
                        inner.extend(patterns[currentPattern][rowsOfPattern])
                        axis2Counter += 1

                    else:
                        outer.append(inner)
                        inner = []
                        print('new inner)')
                        print(f'currentPattern:{currentPattern} rowsOfPattern:{rowsOfPattern}')
                        inner.extend(patterns[currentPattern][rowsOfPattern])
                        axis2Counter = 1
            outer.append(inner)
            inner = []
            patternsInRow += 1
            currentRow += axis2
        return outer

    combinedPatterns = []
    outerRows, outerColumns, added = best_layout(loops)

    if added:
        loops += 1
    for quantity in range(loops):

        if quantity == numberOfPatterns:
            blank = True
        else:
            blank = False
        pattern = pattern_generator(rows, columns, blank)
        patternWithBorder = border_maker(columns, pattern)
        combinedPatterns.append(patternWithBorder)

    output = pattern_display(combinedPatterns, outerRows, outerColumns)

    return output


rows, columns = 12, 8
numberOfPatterns = 7

combined = pattern_combiner(rows, columns, numberOfPatterns)

for i in combined:
    print(i)
print()
