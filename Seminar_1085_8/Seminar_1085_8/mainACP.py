import pandas as pd
import Functii as f
import Grafice as g
import acp.ACP as acp


tabel = pd.read_csv('dataIN/Teritorial.csv', index_col=0)
print(tabel)

# nr. variabile observate utile
m = tabel.columns[1:].size
print(m)
vars = tabel.columns[1:].values
print(vars, type(vars))

# nr. observatii
n = tabel.index.size
print(n)
obs = tabel.index.values
print(obs, type(obs))

X = tabel[vars].values
print(X, type(X), X.shape)
# calcul matrice standardizata variabile observate
X_std = f.standardizare(X)
print(X_std)
# salvati matricea standardizata intr-un fisier CSV
# TODO

# instatiere clasa ACP
modelACP = acp.ACP(X)
# extragere valori proprii
alpha = modelACP.getAlpha()
# apel grafic varianta explicata de componenetele principale
g.valori_proprii(valori=alpha)
# g.afisare()

# extragere componente principale din model
comp = modelACP.getComponente()
# salvati componentele principale intr-un fisier CSV
comp_df = pd.DataFrame(data=comp,
        index=(ob for ob in obs),
        columns=('C'+str(j+1) for j in range(comp.shape[1])))
comp_df.to_csv('./dataOUT/ComponentePrincipale.csv')
# reprezentare grafica componente principale
g.intensitate_legaturi(matrice=comp_df,
                       titlu='Matricea componentelor pricipale')
# g.afisare()

# extragere factori de corelatie (factor loadings)
Rxc = modelACP.getFactorLoadings()
# salvati factor laodings intr-un fisier CSV
Rxc_df = pd.DataFrame(data=Rxc,
        index=(var for var in vars),
        columns=('C'+str(j+1) for j in range(Rxc.shape[1])))
# TODO
# reprezentare grafica a factorilor de corelatie
g.corelograma(R2=Rxc_df, titlu='Factor loadings - corelatie dintre variabilele'
                               'observate si componentele pricipale')
# g.afisare()

# extragere scoruri - componente principale standardizate din model
scoruri = modelACP.getScoruri()
# salvati scoruri intr-un fisier CSV
scoruri_df = pd.DataFrame(data=scoruri,
        index=(ob for ob in obs),
        columns=('C'+str(j+1) for j in range(scoruri.shape[1])))
scoruri_df.to_csv('./dataOUT/Scoruri.csv')
# reprezentare grafica a scorurilor
g.intensitate_legaturi(matrice=scoruri_df, color='Blues',
           titlu='Matricea scorurilor - componente pricipale standardizate')
# g.afisare()

# extragere comunalitati
comun = modelACP.getComunalitati()
# salvati comunalitati intr-un fisier CSV
comun_df = pd.DataFrame(data=comun,
            index=(var for var in vars),
            columns=('C' + str(j + 1) for j in range(comun.shape[1])))
# TODO
# reprezentare grafica a comunalitatilor
g.corelograma(R2=comun_df, titlu='Matricea comunalitatilor')
# g.afisare()

# creare cerc al corelatiilor pentru C1 si C2
g.cercul_corelatiilor(R2=Rxc_df)
g.cercul_corelatiilor(R2=Rxc_df, V1=0, V2=2)
g.afisare()