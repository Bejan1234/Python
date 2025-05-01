# script pentru testul selectiei generatiei urmatoare - selectia de tip elitist
import numpy as np
import generare_init as gi
import matplotlib.pyplot as grafic


def elitism(Pop_curenta,Cal_pc,Pop_copii,Cal_copii,dimensiune):
    Gen_urm=Pop_copii.copy()
    Cal_urm=Cal_copii.copy()
    max_curent=max(Cal_pc)
    max_copii=max(Cal_copii)
    if max_curent>max_copii:
        poz=np.argmax(Cal_pc)
        poz_inlocuita=np.random.randint(dimensiune)
        Gen_urm[poz_inlocuita]=Pop_curenta[poz].copy()
        Cal_urm[poz_inlocuita]=Cal_pc[poz]
    return Gen_urm, Cal_urm

#generarea aleatoare a doua populatii
dim=6
n=16
p1=gi.gen(n,dim)
p2=gi.gen(n,dim)
genu,valori=elitism(p1[:,:n],p1[:,n],p2[:,:n],p2[:,n],dim)
#constituirea populatiei rezultate
rez=np.zeros([dim,n+1],dtype='int')
rez[:,:n]=genu.copy()
rez[:,n]=valori.copy()
print('populatia1')
print(p1)
print('populatia2')
print(p2)
print('selectat:')
print(rez)

x=[i for i in range(dim)]
grafic.plot(x,p1[:,n],"go",markersize=18,label='Populatia curenta')
grafic.plot(x,p2[:,n],"bo",markersize=14,label='Copiii eventual mutati')
grafic.plot(x,rez[:,n],"ro",markersize=10,label='Generatia urmatoare')
grafic.legend()
grafic.show()
