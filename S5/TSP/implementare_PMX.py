import numpy as np

#descriere PMX - varianta
#echivalent cu functia crossover_PMX din FunctiiCrossoverIndivizi

def c_PMX(x,y,p1,p2):
    n=x.size
    copil=-np.ones(n,dtype="int")
    copil[p1:p2+1]=x[p1:p2+1]
    #pozitiile alelelor din secventa de crossover din y care nu apartin lui copil
    poz_alele_neplasate=[k for k in range(p1,p2+1) if not y[k] in copil]
    for p in poz_alele_neplasate:
        a=y[p]
        while copil[p]>-1:
            p=np.where(y==copil[p])[0][0]
        copil[p]=a
    alele_neplasate=[y[k] for k in range(n) if not y[k] in copil]
    pozitii_libere=[k for k in range(n) if copil[k]==-1]
    copil[pozitii_libere]=alele_neplasate.copy()
    return copil

def PMX(x,y):
    n=len(x)
    i=np.random.randint(0,n-1)
    j=np.random.randint(i+1,n)
    print(i,j)
    c1=c_PMX(x,y,i,j)
    c2=c_PMX(y,x,i,j)
    return c1,c2

if __name__=="__main__":
    n=10
    x=np.random.permutation(n)
    y=np.random.permutation(n)
    print("parinte1:",x)
    print("parinte2:", y)
    c1,c2=PMX(x,y)
    print("copil1:  ", c1)
    print("copil2:  ", c2)
