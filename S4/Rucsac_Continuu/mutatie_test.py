import numpy as np
from FunctiiMutatieIndivizi import m_neuniforma
import matplotlib.pyplot as grafic
import random
import copy


#verifica fezabilitatea alegerii x si calculeaza si f. obiectiv
def ok(x,c,v,max):
    val=np.dot(x,v)
    cost=np.dot(x,c)
    return cost<=max, val




#genereaza populatia initiala
#I:
# fc, fv - numele fisierelor cost, valoare
# max - capacitatea maxima
# dim - numarul de indivizi din populatie
# E:
# c,v - parametri de iesire necesari in rezolvarea problemei
#pop - populatia insotita de calitati

def gen(fc,fv,max,dim):
    #citeste datele din fisierele cost si valoare
    c=np.genfromtxt(fc)
    v = np.genfromtxt(fv)
    #n=dimensiunea problemei
    n=v.size
    #lucreaza cu populatia ca lista de dim elemente - liste cu cate n+1 indivizi
    pop=[]
    for i in range(dim):
        gata=False
        while gata == False:
            #genereaza candidatul x cu elemente 0,1
            #x=[random.choice([0,1]) for _ in range(n)]
            x=[random.uniform(0,1) for _ in range(n)]
            gata,val=ok(x,c,v,max)
        #am gasit o solutie candidat fezabila, in data de tip lista x
        # adauga valoarea
        x.append(val)
        #adauga la populatie noul individ cu valoarea f. obiectiv - adauga inca o lista cu n+1 elemente ca element al listei pop
        pop.append(x)
    ind = [i for i in range(dim)]
    vectv=[pop[i][-1] for i in range(dim)]
    grafic.plot(ind, vectv, "gs", markersize=11,label="Initial")
    return pop, c, v


def mutatie_populatie(pop,c,v,max,pm,sigma):
    # copiem populatia curenta in rezultatul mpop
    mpop=copy.deepcopy(pop)
    dim=len(pop)
    n=c.size
    #adun valorile indivizilor mutati pentru reprerzentarea grafica
    valv=[]
    for i in range(dim):
        #copiem in x individul i
        x=pop[i][:n].copy()
        mutat=False
        for j in range(n):
            #genereaza aleator daca se face mutatie in individul i gena j
            r=np.random.uniform(0,1)
            if r<=pm:
                #mutatie neuniforma
                x[j]=m_neuniforma(x[j],sigma,0,1)
                mutat=True
        #individul rezultat sufera posibil mai multe mutatii
        #daca este fezabil, este pastrat
        if mutat:
            fez, val = ok(x,c, v, max)
            if fez:
                x=x+[val]
                mpop.append(x)
                valv=valv+[val]
            else:
                #nu modific nimic in populatie
                valv=valv+[pop[i][n]]
        else:
            # nu modific nimic in populatie
            valv = valv + [pop[i][n]]
    ind=[i for i in range(dim)]
    grafic.plot(ind,valv,"rs",markersize=9,label="Dupa mutatie")
    return mpop


if __name__=="__main__":
    max=50
    dim=10
    p,c,v=gen("cost.txt","valoare.txt",max,dim)
    o=mutatie_populatie(p,c,v,max,0.8,0.7)
    grafic.legend()
    grafic.show()


