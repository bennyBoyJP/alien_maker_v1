def pattern_combiner(rows, columns, loops):

    def border_maker(y, inside):

        for item in inside:
            item.insert(0, 9)
            item.append(9)

        topBottomRow = [9 for iterations in range(y + 2)]

        inside.insert(0, topBottomRow)
        inside.append(topBottomRow)
        return inside

    def best_layout(number_of_patterns):
        return 1, 1

    def pattern_display(patterns, axis1, axis2):
        return 0

    from amv1_pattern_generator import pattern_generator
    combinedPatterns = []
    for quantity in range(loops):
        pattern = pattern_generator(rows, columns)
        patternWithBorder = border_maker(columns, pattern)

        combinedPatterns.append(patternWithBorder)
    outerRows, outerColumns = best_layout(loops)
    output = pattern_display(combinedPatterns, outerRows, outerColumns)

    return combinedPatterns

rows, columns = 12, 8
numberOfPatterns = 1

combined = pattern_combiner(rows, columns, numberOfPatterns)
print()
for i in range(len(combined)):
    for j in combined[i]:
        print(str(j).center(150))
    print()
