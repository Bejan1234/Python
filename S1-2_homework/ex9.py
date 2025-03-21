import numpy as np

# Generăm matricea A cu 20 de linii și 7 coloane (valori 0 sau 1)
A =np.random.randint(0,2,(20,7))
V = np.sum(A,axis=1)
print("Matricea A:")
print(A)
print("\nVectorul V:")
print(V)