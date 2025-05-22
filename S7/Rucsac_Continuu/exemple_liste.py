# Liste comprehensive - exemple

#generarea unei liste care contine o progresie aritmetica 45...-34 cu ratia -5
L=[i for i in range(45,-34,-5)]
#selectarea elemetelor divizibile cu k din lista
k=3
LP=[x for x in L if x%k==0]
#calculu maximului din lista si determinarea pozitiei de aparitie
maxim=max(L)
index=L.index(maxim)
print("Lista L:",L)
print("Elementele divizibile cu 3 din L:",LP)
print("\nMaximul este ",maxim," si apare in pozitia ",index)

# toate pozitiile de aparitie ale unui element intr-o lista
t=[1,2,3,4,1,2,3,4,1,2,3,4,3,2,1]
toate_poz=[i for i, j in enumerate(t) if j == 3]
# i pozitie in t, j valoare
print("\n3 apare in lista",t)
print("in pozitiile:",toate_poz)


#generarea unei multimi de tipul -1, -1+eps, -1+2*eps, ..., 1
eps=0.1
L1=[-1+i*eps for i in range(10000) if -1+i*eps<=1]
print("\nValorile din [-1,1] cu pas 0.1", L1)

# alternativ, folosind numpy
import numpy
L2=numpy.arange(-1,1+0.1,0.1)
print("\nValorile din [-1,1] cu pas 0.1", L2)
