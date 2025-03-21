def insertion_sort(column):
    for i in range(1, len(column)):
        key = column[i]
        j = i - 1
        while j >= 0 and column[j] > key:
            column[j + 1] = column[j]
            j -= 1
        column[j + 1] = key


def sort_columns(matrix):
    num_rows = len(matrix) #3 randuri
    num_cols = len(matrix[0]) # 4 coloane

    for col in range(num_cols):
        # Extragem elementele coloanei
        column = [matrix[row][col] for row in range(num_rows)]
        # Sortăm coloana
        insertion_sort(column)
        # Reintegram elementele sortate în matrice
        for row in range(num_rows):
            matrix[row][col] = column[row]


# Exemplu de matrice
matrix = [
    [5, 1, 9, 3],
    [8, 2, 7, 4],
    [6, 0, 3, 2]
]

# Sortăm coloanele matricei
sort_columns(matrix)


# Afișăm matricea sortată
for row in matrix:
    print(row)
