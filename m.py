'''Suppose you have a 5 × 5 list that consists of zeros and M’s. Write a program that creates a new 5 × 5 list that has M’s in the same place, but the zeroes are replaced by counts of how many M’s are in adjacent cells (adjacent either horizontally, vertically, or diagonally). An example is shown below. [Hint: short-circuiting may be helpful for avoiding index-out-of-range errors.]
0 M 0 M 0     1 M 3 M 1
0 0 M 0 0       1 2 M 2 1
0 0 0 0 0        2 3 2 1 0
M M 0 0 0      M M 2 1 1
0 0 0 M 0       2 2 2 M 1'''
matrix = [[0, 'M', 0, 'M', 0], 
            [0, 0, 'M', 0, 0], 
            [0, 0, 0, 0, 0], 
            ['M', 'M', 0, 0, 0], 
            [0, 0, 0, 'M', 0]]

new_matrix = []

for i in range(5):
    line = []
    for j in range(5):
        if matrix[i][j] == 'M':
            line.append('M')
        else:
            #Этот сегмент кода сложно понять мне. Ну очень.
            count = 0
            for x in range(max(0, i-1), min(5, i+2)):
                for y in range(max(0, j-1), min(5, j+2)):
                    if matrix[x][y] == 'M':
                        count += 1
            line.append(count)
    new_matrix.append(line)
    #################################################################

for n in new_matrix:
    print(n)