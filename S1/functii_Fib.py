#sirul lui Fibonacci
# fib[0]=0, fib[1]=1, fib[n]=fib[n-1]+fib[n-2]

#recursiv - doar termenul n
def Fib0(n):
    if n==0:
        rez=0
    elif n==1:
        rez=1
    else:
        rez=Fib0(n-1)+Fib0(n-2)
    return rez

#vectori - nerecursiv
import numpy as np

def Fib1(n):
    rez=np.zeros(n+1,dtype='int')
    rez[1]=1
    for i in range(2,n+1):
        rez[i]=rez[i-1]+rez[i-2]
    return rez

#liste - nerecursvi
def Fib2(n):
    rez=[0,1]
    for i in range(2,n+1):
        rez.append(rez[i-1]+rez[i-2])
        #rez=rez+[rez[i-1]+rez[i-2]]
    return rez


if __name__=="__main__":
    n=int(input("n="))
    sir_F=Fib2(n)
    print("Sirul lui Fibonacci ",sir_F)
