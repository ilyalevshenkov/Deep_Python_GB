#Напишите функцию для транспонирования матрицы transposed_matrix,
#принимает в аргументы matrix, и возвращает транспонированную матрицу.
def transpose(matrix):
    # Determine the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with dimensions swapped
    transposed = [[0 for row in range(rows)] for col in range(cols)]

    # Fill the new matrix with values from the old matrix
    for row in range(rows):
        for col in range(cols):
            transposed[col][row] = matrix[row][col]

    return transposed
# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

#Call the transpose function
transposed_matrix = transpose(matrix)

# Display the contents of the transposed matrix
for row in transposed_matrix:
    print(row)