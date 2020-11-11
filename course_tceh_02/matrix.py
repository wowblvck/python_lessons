matrix = [[3, 65, 18, 52],
          [13, 35, 98, 82],
          [97, 25, 72, 44]]

print('Strings:')
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print("{:4d}".format(matrix[i][j]), end=" ")
    print('\n')

print('Column:')
revert_matrix = list(zip(*matrix))
for i in range(len(revert_matrix)):
    for j in range(len(revert_matrix[i])):
        print("{:4d}".format(revert_matrix[i][j]), end=" ")
    print('\n')
