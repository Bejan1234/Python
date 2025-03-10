# copiati tot codul in consola pentru a vedea valorile fiecarei variabile

import numpy as np

#generare aleatoare vector - 25 intregi intre -3 si 10

v=np.random.randint(-3,11,25)

#generare aleatore matrice - 3x4, elemente generate uniform pe [-2,7]

a=np.random.uniform(-2,7,[3,5])

#calcul element maxim

maxim_v1=v.max()

maxim_a=a.max()

#cautare valoarea 5 in vector

poz1=np.argwhere(v==5)
# poz1 are numar aparitii linii si o coloana

for x in poz1:
    print(x[0])

#cautare valoarea a[0,0] in matrice

poz2=np.argwhere(a==a[0,0])
# poz1 are numar aparitii linii si doua coloane
for x in poz2:
    print(x[0],x[1])

#sortare vector
v_sort=np.sort(v)


#sortare matrice dupa ultima coloana
indici=a[:,-1].argsort()
b=a[indici]

#valoare medie vector
val_medie=np.mean(v)

#deviatie standard vector
dev_std=np.std(v)

#vectorul valorilor medii pe fiecare din cele 3 linii ale lui a
med_linii=np.zeros(3)
for i in range(3):
    med_linii[i]=np.mean(a[i])


