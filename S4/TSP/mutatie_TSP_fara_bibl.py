import numpy as np
import matplotlib.pyplot as grafic

#f. obiectiv
def foTSP(p,c):
    n=p.size
    cost=c[p[0],p[-1]]
    for i in range(n-1):
        cost+=c[p[i],p[i+1]]
    return 100/cost



def gen(fc,dim):
    c=np.genfromtxt(fc)
    n=c.shape[0]
    populatie=np.zeros([dim,n],dtype="int")
    valori=np.zeros(dim)
    for i in range(dim):
       populatie[i]=np.random.permutation(n)
       valori[i] = foTSP(populatie[i],c)
    ox=[i for i in range(dim)]
    oy=valori
    grafic.plot(ox,oy,"gs",markersize=11,label="Initial")
    return populatie, valori, c


def mutatie_inversiune(p,c):
    n=p.size
    print(f"Individul initial {p}")
    i=np.random.randint(0,n-1)
    j=np.random.randint(i+1,n)
    print(f"Pozitiile de mutatie: {i} , {j}")
    r=p.copy()
    r[i:j+1]=[p[k] for k in range(j,i-1,-1)]
    print(f"Individul dupa mutatie {r}\n")
    return r


def mutatie_populatie(pcopii,vcopii,c,pm):
    mpo=pcopii.copy()
    mvo=vcopii.copy()
    dim=mpo.shape[0]
    for i in range(dim):
        r=np.random.uniform(0,1)
        if r<=pm:
            x=mpo[i]
            y=mutatie_inversiune(x,c)
            mpo[i]=y
            mvo[i]=foTSP(y,c)
    grafic.plot([i for i in range(dim)],mvo,"rs",markersize=10,label="Dupa mutatie")
    return mpo,mvo

if __name__=="__main__":
    p,v,c=gen("costuri.txt",20)
    o,vo=mutatie_populatie(p,v,c,0.2)
    grafic.legend()
    grafic.show()