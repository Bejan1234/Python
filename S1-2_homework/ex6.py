import numpy as np

#Definirea matricei A si B si n

n =2

A = np.array([[1,2],
             [3,4]])
B = np.array ([[5,6],
              [7,8]])

#1.Calculul transpusei lui A (A^T)
A_T=A.T
print("Transpusa lui A (A>T:")
print(A_T)

#2.Calculul sumei A+B
A_plus_B= A+B
print("\nSuma A+B este:")
print(A_plus_B)

#3.Calculul produsului A*B
A_produs_B=np.dot(A,B)
print("\nProsusul A * B este:")
print(A_produs_B)

#4.Calculul puterii A*2
A_squered=np.dot(A,n)
print("\nA*2 este: ")
print(A_squered)