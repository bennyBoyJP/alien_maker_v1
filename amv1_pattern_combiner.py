def pattern_combiner(rows, columns, loops, border):

    from amv1_pattern_generator import pattern_generator

    def border_maker(y, inside, border):

        for item in inside:
            for repeater in range(border):
                item.insert(0, 9)
                item.append(9)

        topBottomRow = [9 for iterations in range(y + (border * 2))]

        for repeater in range(border):
            inside.insert(0, topBottomRow)
            inside.append(topBottomRow)
        return inside

    def best_layout(number_of_patterns):

        addedPattern = False
        if number_of_patterns == 1:
            return 1, 1, addedPattern
        elif number_of_patterns == 2:
            return 1, 2, addedPattern

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
                        # print(f'currentPattern:{currentPattern} rowsOfPattern:{rowsOfPattern}')
                        inner.extend(patterns[currentPattern][rowsOfPattern])
                        axis2Counter += 1

                    else:
                        outer.append(inner)
                        inner = []
                        # print('new inner)')
                        # print(f'currentPattern:{currentPattern} rowsOfPattern:{rowsOfPattern}')
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
        patternWithBorder = border_maker(columns, pattern, border)
        combinedPatterns.append(patternWithBorder)

    output = pattern_display(combinedPatterns, outerRows, outerColumns)

    return output


patternRows, patternColumns = 8, 8
numberOfPatterns = 2
borderWidth = 1



# print(f'rows: {len(combined)}')
# print(f'columns: {len(combined[0])}')

#----
import pygame
import os
import time

pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = '1'

clock = pygame.time.Clock()
fps = 24

automata = True
while automata:
    clock.tick(fps)


    combined = pattern_combiner(patternRows,patternColumns,numberOfPatterns,borderWidth)
    screen_rows = len(combined)
    screen_columns = len(combined[0])

    cellScale = 50
    cellOffset = 0

    screenWidth, screenHeight = (screen_columns * cellScale), (screen_rows * cellScale)
    screenSize = (screenWidth,screenHeight)
    screen = pygame.display.set_mode(screenSize)

    gridColor = (0, 0, 0)
    background = (0, 0, 0)
    patternColor = (200, 200, 200)
    borderColor = (0, 0, 0)
    screen.fill(gridColor)


    def print_generation(rows, columns, array, print_screen, print_background, color, border, scale, offset):

        for x in range(rows):
            for y in range(columns):

                y_pos = y * scale
                x_pos = x * scale

                if array[x][y] == 1:
                    pygame.draw.rect(print_screen, color,[y_pos,x_pos,scale - offset,scale - offset])

                if array[x][y] == 0:
                    pygame.draw.rect(print_screen, print_background,[y_pos,x_pos,scale - offset,scale - offset])

                if array[x][y] == 9:
                    pygame.draw.rect(print_screen, border, [y_pos,x_pos,scale - offset,scale - offset])



    print_generation(screen_rows, screen_columns, combined, screen, background, patternColor, borderColor, cellScale, cellOffset)
    pygame.display.update()
    time.sleep(.01)