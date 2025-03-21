from itertools import permutations
import math

arr = [1, 2, 3, 8, 3, 4, 5, 6]  # Lista de elemente
n = len(arr)  # Numărul de elemente

# Calculăm numărul total de permutări
num_permutations = math.factorial(n)

# Generăm și afișăm toate permutările
perm = list(permutations(arr))

print(f"Numărul total de permutări: {num_permutations}")
print("Permutările sunt:")
for p in perm:
    print(p)
