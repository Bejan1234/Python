#crearea unor masive cu elemente numere aleatoare
import numpy as np

#vector cu 5 numere aleatoare, intre 10 si 19
v=np.random.randint(10,20,5)

#matrice mxn cu numere generate uniform in intervalul [-5.4)
m=3
n=2
a=np.random.uniform(-5,4,[m,n])

#constructia unei matrice mX(n+1)
#zona mxn generata aleator din distributia N(0,1)
#pe ultima coloana: suma elementelor fiecarei linii

#initializare cu matricea cu toate elementele 0
matrice=np.zeros([m,n+1])
#generarea aleatoare in zona mxn
matrice[:m,:n]=np.random.normal(0,1,[m,n])
for i in range(m):
    matrice[i,n]=sum(matrice[i,:n])
print(matrice)
