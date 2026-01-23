import numpy as np
import pandas as pd
from tensorboard.compat.tensorflow_stub.tensor_shape import vector

import utile as utl
import aef.AEF as aef
import factor_analyzer as fa
import Grafice as g
from sklearn.preprocessing import StandardScaler


tabel = pd.read_csv('dataIN/MortalityEU.csv',
                    index_col=0, na_values=':')
print(tabel)

# extragere etichete linii
obsNume = tabel.index.values
print(obsNume, type(obsNume), obsNume.shape)
# extragre etichete coloane
varNume = tabel.columns.values
print(varNume, type(varNume), varNume.shape)
matrice_numerica = tabel.values
print(type(matrice_numerica), matrice_numerica.shape)

# nr. observatii
n = matrice_numerica.shape[0]
print('nr. observatii:', n)
# nr. de variabile
m = len(varNume)
print('nr. de variabile', m)

# inlocuire celule NAN
X = utl.inlocuireNAN(matrice_numerica)
# salvare matrice initiala in fisier CSV
X_df = pd.DataFrame(data=X, index=obsNume, columns=varNume)
X_df.to_csv(path_or_buf='./dataOUT/X.csv')

# standardizare matrice initiala
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
# salvare matrice initiala standardizata
X_std_df = pd.DataFrame(data=X_std, index=obsNume, columns=varNume)
X_std_df.to_csv(path_or_buf='./dataOUT/X_std.csv')

# calculam testul de sfericitate Bartlett
sfericitate = fa.calculate_bartlett_sphericity(x=X_std)
print(sfericitate, type(sfericitate))
if sfericitate[0] > sfericitate[1]:
    print('Exista cel putin un factor comun!')
else:
    print('Nu exista nici un factor comun!')
    exit(-1)

# calcul indici de factorabilitate Kaiser-Meyer-Olkin (KMO)
kmo = fa.calculate_kmo(x=X_std)
print(kmo, type(kmo))
if kmo[1] > 0.5:
    print('Variabilele observate pot fi exprimate prin factori comuni!')
else:
    print('Nu exista factori comuni!')
    exit(-2)

# creare matrice cu o singura coloana dintr-un vector
vector = kmo[0]
print(type(vector), vector.shape)
matrice = vector[:, np.newaxis]
print(matrice, type(matrice), matrice.shape)
# construire grafic de tip intensitate legatura
matrice_df = pd.DataFrame(data=matrice, index=varNume,
                          columns=['Indici KMO'])
g.intesitate_legatura(matrice=matrice_df, titlu='Indici Kaiser-Meyer-Olkin')
g.afisare()


# TODO