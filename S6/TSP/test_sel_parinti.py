# script pentru testul selectiei parintilor - selectia de tip SUS cu distributie fps cu sigma-scalare
import numpy as np
from FunctiiSelectii import *

import generare_init as gi
import matplotlib.pyplot as grafic


#generarea aleatoare a unei populatii
dim=12
p,v,n=gi.gen("costuri.txt",dim)
# calculul parintilor si calitatii acestora utilizand selectia SUS cu FPS cu sigma-scalare
parinti,valori=SUS(p,v,dim,n)


x=range(dim)
grafic.plot(x,v,"go",markersize=16,label='Calitatile populatiei curente')
grafic.plot(x,valori,"ro",markersize=10,label='Calitatile parintilor')
grafic.legend()
grafic.show()