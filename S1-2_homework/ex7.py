import numpy as np


def insertion_sort(arr):
    for i in range(1, len(arr)):  # Începem de la al doilea element
        key = arr[i]
        j = i - 1

        # Deplasăm elementele mai mari decât key către dreapta
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Inserăm elementul în poziția corectă


# Exemplu de utilizare
arr = [5, 3, 8, 6, 2, 7, 4, 1]
insertion_sort(arr)
print("Lista sortată:", arr)
