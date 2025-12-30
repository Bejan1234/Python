'''
Clasa care incapsuleaza implementarea modelului de ACP
'''
import numpy as np
from Seminar_1085_8 import Functii as f


class ACP:
    def __init__(self, X):
        # asumam ca primim un numpy.ndarray
        # calcul matrice coeficienti de corelatie
        self.corr = np.corrcoef(x=X, rowvar=False) # avem variabilele pe coloane
        print(self.corr, self.corr.shape)
        # standardizare matrice variabile observate
        self.X_std = f.standardizare(X)
        print(self.X_std.shape)
        # calcul matrice de varianta-covarianta pe X standardizat
        self.cov = np.cov(m=self.X_std, rowvar=False)
        # calcul valori si vectorii proprii pentru matricea de varianta-covarianta
        valori, vectori = np.linalg.eigh(a=self.cov)
        print(valori)
        print(vectori.shape)
        # sortare descrascatpare a valorilor proprii
        # si a vectorilor proprii
        k_desc = [k for k in reversed(np.argsort(a=valori))]
        print(k_desc)
        self.alpha = valori[k_desc]
        print(self.alpha)
        self.a = vectori[:, k_desc]
        # regularizarea vectorilor proprii
        # pentru min pe coloana mai mare decat max pe coloana
        # in valoare absoluta, inmultim vectorul propriu cu -1
        for j in range(self.a.shape[1]):
            min = np.min(self.a[:, j])
            max = np.max(self.a[:, j])
            if np.abs(min) > np.abs(max):
                self.a[:, j] = -self.a[:, j]

        # calcul componente principale
        self.C = self.X_std @ self.a
        # calcul matrice de factor loadings
        # corelatia dintre variabilele observate si componentele principale
        # sau matricea factorilor de corelatie
        self.Rxc = self.a * np.sqrt(self.alpha)


    def getCorr(self):
        return self.corr

    def getStd(self):
        return self.X_std

    def getAlpha(self):
        return self.alpha

    def getVectori(self):
        return self.a

    def getComponente(self):
        return self.C

    def getFactorLoadings(self):
        return self.Rxc

    def getScoruri(self):
        return self.C / np.sqrt(self.alpha)

    def getComunalitati(self):
        # Rxc2 = self.Rxc * self.Rxc
        Rxc2 = np.square(self.Rxc)
        return np.cumsum(a=Rxc2, axis=1) # sume cumulative pe linii
