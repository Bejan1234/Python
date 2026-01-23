import numpy as np


def inlocuireNAN(X):
    # asumam ca X est eun numpy.ndarray
    medii_pe_coloane = np.nanmean(a=X, axis=0)  # avem variabilele pe coloane
    pozitie = np.where(np.isnan(X))
    print(pozitie, type(pozitie))
    X[pozitie] = medii_pe_coloane[pozitie[1]]
    # TODO
    return X
