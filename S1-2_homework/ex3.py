def bubble_sort(arr):
    n = len(arr)  
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def sort_matrix_by_rows(matrix):
    for row in matrix:
        bubble_sort(row)


matrix = [
    [5, 1, 9, 3],
    [8, 2, 7, 4],
    [6, 0, 3, 2]
]

sort_matrix_by_rows(matrix)  # 17

for row in matrix:
    print(row)