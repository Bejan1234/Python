import numpy as np
from FunctiiMutatieIndivizi import m_perm_inserare
import matplotlib.pyplot as grafic


#f. obiectiv
def foNR(x,n):
    # functia obiectiv pentru problema reginelor

    # I: x - individul (permutarea) evaluat(a), n-dimensiunea problemei
    # E: c - calitate (numarul de perechi de regine care nu se ataca

    c = n*(n-1)/2
    for i in range(n):
        for j in range(i+1,n):
            if abs(i-j)==abs(x[i]-x[j]):
                c=c-1
    return c


#genereaza populatia initiala
#I:
# n - dimensiunea prolemei
# dim - numarul de indivizi din populatie
#E: pop - populatia initiala
def gen(n,dim):
    #defineste o variabila ndarray cu toate elementelo nule
    pop=np.zeros((dim,n+1),dtype=int)
    for i in range(dim):
        #genereaza candidatul permutare cu n elemente
        pop[i,:n]=np.random.permutation(n)
        pop[i,n]=foNR(pop[i,:n],n)
    ind = [i for i in range(dim)]
    grafic.plot(ind, pop[:,n], "go", markersize=11, label="Initial")
    return pop


# mutatia prin inserare intr-o permutare
def mutatie_inserare(p,n):
    print(f"\n\n\nmutatie in {p} cu calitatea {foNR(p,n)}")
    p1=np.random.randint(0,n-1)
    p2=np.random.randint(p1+1,n)
    print(f"\npozitiile sunt {p1+1} si {p2+1}")
    rez=p.copy()
    if p1+1<p2:
        element_inserat=p[p2]
        x=np.delete(p,p2)
        rez=np.insert(x,p1+1,element_inserat)
    print(f"\nrezulta individul {rez} cu calitatea {foNR(rez,n)}")
    return rez



#mutatie asupra populatiei de copii
# I:pop,dim,n - populatia de dimensiuni dimx(n+1)
#   pm - probabilitatea de mutatie
#E: - mpop - populatia mutata
def mutatie_populatie(pop,dim,n,pm):
    mpop=pop.copy()
    for i in range(dim):
        #genereaza aleator daca se face mutatie
        r=np.random.uniform(0,1)
        if r<=pm:
            #mutatie in individul i - prin inserare
            x=m_perm_inserare(mpop[i,:n],n)
            mpop[i,:n]=x.copy()
            mpop[i,n]=foNR(x,n)
    ind = [i for i in range(dim)]
    grafic.plot(ind, mpop[:,n], "ro", markersize=9,label="Dupa mutatie")
    return mpop

if __name__=="__main__":
    p=gen(12,20)
    o=mutatie_populatie(p,20,12,0.25)
    grafic.legend()
    grafic.show()


