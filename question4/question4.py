#Hi, I wrote this code by python

# Get the size of the matrix from the user
m = int(input('Enter the number of rows: '))
n = int(input('Enter the number of columns: '))

matrix = []         # Initialize the matrix and list to store zero coordinates
zeroes_coordinate = []

for i in range(m):          # Populate the matrix with user input
    row_list = []
    for j in range(n):
        member = int(input(f'Row {i}, enter the {j}th member: '))
        if member == 0:
            zeroes_coordinate.append([i, j])
        row_list.append(member)
    matrix.append(row_list)

for a in zeroes_coordinate:         # Set zeroes in the matrix based on zero coordinates
    for i in range(n):
        matrix[a[0]][i] = 0
    for j in range(m):
        matrix[j][a[1]] = 0

# Print the modified matrix
print(matrix)