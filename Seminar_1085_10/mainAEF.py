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
# extragere etichete coloane
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
# g.afisare()

modelAEF = aef.AEF(matrice=X)
# identificarea nnumarului de factori seminicativi care pot extrasi
nr_semnicativ_factori = 2
chi2TabMin = 1
for k in range(nr_semnicativ_factori, m):
# for k in range(nr_semnicativ_factori, 6):
    modelFA = fa.FactorAnalyzer(n_factors=k)
    modelFA.fit(X=X_std)
    print(modelFA.loadings_, )
    chi2Calc, chi2Tab = modelAEF.calculTestBartlett(modelFA.loadings_,
                                modelFA.get_uniquenesses())
    print(chi2Calc, chi2Tab)

    if np.isnan(chi2Calc) or np.isnan(chi2Tab):
        break

    if chi2Tab < chi2TabMin:
        chi2TabMin = chi2Tab
        nr_semnicativ_factori = k

print('Nr. semnificativ de factori ce pot fi extrasi:', nr_semnicativ_factori)

# creare model cu numarul semnifactiv de factori determinat
modelFitFA = fa.FactorAnalyzer(n_factors=nr_semnicativ_factori)
modelFitFA.fit(X=X_std)
factor_loadings = modelFitFA.loadings_
# avem acum disponibila matricea de corelatie a variabilellor observate
# cu factorii extrasi
factor_loadings_df = pd.DataFrame(data=factor_loadings,
                    index=varNume,
                    columns=('F'+str(j+1) for j in range(nr_semnicativ_factori)))
factor_loadings_df.to_csv('./dataOUT/FactorLoadings.csv')
g.corelograma(R2=factor_loadings_df, titlu='Corelograma factorilor de corelatie')
# g.afisare()

# extragre valori proprii pentru reliefarea variantei explicate de catre factori
alpha = modelFitFA.get_eigenvalues()
print(alpha, type(alpha))
g.valori_proprii(valori=alpha[0])
# g.afisare()

# calcul scoruri din AEF (componentele principale standardizate)
scoruri = modelAEF.getScoruri()
scoruri_df = pd.DataFrame(data=scoruri, index=obsNume,
                columns=('C'+str(j+1) for j in range(scoruri.shape[1])))
scoruri_df.to_csv(path_or_buf='./dataOUT/Scoruri.csv')
g.intesitate_legatura(matrice=scoruri_df, titlu='Matricea scorurilor')

# calitatea reprezentarii observatiilor pe axele componentelor principale
cal_obs = modelAEF.getCalObs()
print(cal_obs.shape)
cal_obs_df = pd.DataFrame(data=cal_obs, index=obsNume,
                columns=('C'+str(j+1) for j in range(scoruri.shape[1])))
cal_obs_df.to_csv(path_or_buf='./dataOUT/CalitateaReprezentariiObservatiilor.csv')
g.intesitate_legatura(matrice=cal_obs_df, titlu='Calitatea reprezentarii '
                                                'observatiilor pe axele componentelor principale')
g.afisare()
# TODO