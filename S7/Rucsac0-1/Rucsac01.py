import numpy as np
import copy
import matplotlib.pyplot as grafic
from FunctiiCrossoverIndivizi import crossover_uniform, crossover_unipunct
from FunctiiMutatieIndivizi import m_binar
from FunctiiSelectii import elitism, ruleta


#verifica fezabilitatea alegerii x si calculeaza si f. obiectiv
def ok(x,c,v,max):
    val=np.dot(x,v)
    cost=np.dot(x,c)
    return cost<=max,val


#genereaza populatia initiala
#I:
# fc, fv - numele fisierelor cost, valoare
# max - capacitatea maxima
# dim - numarul de indivizi din populatie
#E: pop, cal - populatia initiala, calitatile acesteia
def gen(fc,fv,max,dim):
    #citeste datele din fisierele cost si valoare
    c=np.genfromtxt(fc)
    v=np.genfromtxt(fv)
    #n=dimensiunea problemei
    n=len(c)
    #lucreaza cu populatia ca lista de dim elemente - liste cu cate n indivizi
    pop=[]
    cal=[]
    for i in range(dim):
        gata=False
        while gata == False:
            #genereaza candidatul x cu elemente 0,1
            x=np.random.randint(0,2,n)
            gata,val=ok(x,c,v,max)
        #am gasit o solutie candidat fezabila, in data de tip ndarray (vector) x
        # x este transformat in lista
        x=list(x)
        # adauga valoarea
        cal=cal+[val]
        #adauga la populatie noul individ
        pop=pop+[x]
    return pop,cal,c,v



#crossover pe populatia de parinti pop
# I: pop,cal - ca mai sus
#     c, v, max - datele problemei
#     pc- probabilitatea de crossover
#E: po, co - populatia copiilor, calitatile copiilor
# este implementata recombinarea asexuata
def crossover_populatie(pop,cal,c,v,max,pc):
    dim=len(pop)
    n=c.size
    po=copy.deepcopy(pop)
    co=copy.deepcopy(cal)
    #populatia este parcursa astfel incat sunt selectati indivizii 0,1 apoi 2,3 s.a.m.d
    for i in range(0,dim-1,2):
        #selecteaza parintii
        x = copy.deepcopy(pop[i])
        y = copy.deepcopy(pop[i+1])
        r = np.random.uniform(0,1)
        if r<=pc:
            # crossover x cu y - uniform: mai potrivit aici
            c1,c2=crossover_uniform(x ,y ,n)
            fez, val = ok(c1, c, v, max)
            if fez:
                po[i]=copy.deepcopy(c1)
                co[i]=val
            fez, val = ok(c2, c, v, max)
            if fez:
               po[i+1]=copy.deepcopy(c2)
               co[i+1]=val
    return po,co


#mutatie asupra populatiei de copii
# I:pop,cal - matricea populatie si vectorul calitatilor
#   pm - probabilitatea de mutatie
#E: - mpop - populatia mutata, calitatile in aceasta
def mutatie_populatie(pop,cal, c,v,max,pm):
    #copiem populatia in rezultat
    dim = len(pop)
    n = c.size
    mpop=copy.deepcopy(pop)
    mcal=copy.deepcopy(cal)
    for i in range(dim):
        #copiem in x individul i din populatia intrare
        x=copy.deepcopy(pop[i])
        for j in range(n):
            #genereaza aleator daca se face mutatie in individul i gena j
            r=np.random.uniform(0,1)
            if r<=pm:
                #mutatie
                x[j]=m_binar(x[j])
        #individul rezultat sufera posibil mai multe mutatii
        #daca este fezabil, este pastrat
        fez, val = ok(x, c, v, max)
        if fez:
            mpop[i]=copy.deepcopy(x)
            mcal[i]=val
    return mpop, mcal


def arata(sol,v):
    # vizualizare rezultate Rucsac 0-1
    n=len(sol)
    t=len(v)
    val=max(v)
    print("Cea mai buna valoare calculată: ",val)
    print("Alegerea corespunzatoare este: ",sol)
    fig=grafic.figure()
    x=[i for i in range(t)]
    y=[v[i] for i in range(t)]
    grafic.plot(x,y,'ro-')
    grafic.ylabel("Valoarea")
    grafic.xlabel("Generația")
    grafic.title("Evoluția calității celui mai bun individ din fiecare generație")
    grafic.show()



##ALGORITMUL GENETIC PENTRU REZOLVAREA PROBLEMEI RUCSACULUI 0-1
#I: fc,fv - fisierele cu costuri/valori
#   dim - dimensiunea unei populatii
#   NMAX - numarul maxim de simulari ale unei evolutii
#   pc - probabilitatea de crossover
#   pm - probabilitatea de mutatie
#
#E: sol - solutia calculata de GA
#   val - maximul functiei fitness

def GA(fc,fv,cmax,dim,NMAX,pc,pm):
    #generarea populatiei la momentul initial
    pop,cal,c,v=gen(fc, fv, cmax, dim)
    n = c.size
    #initializari pentru GA
    it=0
    gata=False
    nrm=1
    #in istoric_v pastram cel mai bun cost din populatia curenta, la fiecare moment al evolutiei
    istoric_v=[max(cal)]
    # evolutia - cat timp
    #                - nu am depasit NMAX  si
    #                - populatia are macar 2 indivizi cu calitati diferite  si
    #                - in ultimele NMAX/3 iteratii s-a schimbat macar o data calitatea cea mai buna
    while it<NMAX and not gata:
        #SELECTIA PARINTILOR
        spop, sval = ruleta(pop, cal, dim, n)
        # RECOMBINAREA
        pop_o, cal_o = crossover_populatie(spop,sval,c, v, cmax, pc)
        # MUTATIA
        pop_mo,cal_mo = mutatie_populatie(pop_o,cal_o,c,v,cmax,pm)
        # SELECTIA GENERATIEI URMATOARE
        newpop, newval = elitism(pop, cal, pop_mo, cal_mo, dim)
        minim=min(newval)
        maxim=max(newval)
        if maxim==istoric_v[it]:
            nrm=nrm+1
        else:
            nrm=1
        if maxim==minim or nrm==int(NMAX/3):
            gata=True
        else:
            it=it+1
        istoric_v.append(max(newval))
        pop =copy.deepcopy(newpop)
        cal =copy.deepcopy(newval)
    #solutia = cel mai bun individ din ultima generatie
    best=max(cal)
    i_sol = np.argmax(cal)
    sol=pop[i_sol]
    arata(sol,istoric_v)
    return sol,best


if __name__=="__main__":
    sol,val=GA("cost1.txt","valoare1.txt",50,40,100,0.8,0.1)