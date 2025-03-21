import numpy as np

# Exemplu de matrice A și vector V
A = np.array([[1, 3, 2], [4, 6, 5], [7, 9, 8]])
V = np.array([2, 1, 3])

# Sortăm matricea A pe baza valorilor din vectorul V
sorted_indices = np.argsort(V)
A_sorted = A[sorted_indices]

# Afișăm matricea A sortată
print(A_sorted)