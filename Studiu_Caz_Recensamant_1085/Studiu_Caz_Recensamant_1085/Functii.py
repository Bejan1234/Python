import numpy as np


def indice_disimilaritate(table, cols):
    # asumam ca primim ca parametri
    # un pandas.DataFrame si o lista de coloane utile
    X = table[cols].values
    print(X, type(X), X.shape)
    # calcul sume pe linii, pentru fiecare localitate
    SL = np.sum(a=X, axis=1) # facem suma pe linii
    print(SL, SL.shape)
    R = np.transpose(SL - X.T)
    print(R.shape)
    # facem sume pe coloane
    Tx = np.sum(a=X, axis=0)  # sume pe coloane
    print(Tx, Tx.shape)
    Tr = np.sum(a=R, axis=0)  # sume pe coloane
    print(Tr, Tr.shape)
    popRO = Tx + Tr
    print(popRO)
    # inlocuim pentru impartire valorile zero cu 1
    Tx[Tx==0] = 1
    Tr[Tr==0] = 1
    Px = X / Tx
    Pr = X / Tr
    print(Px.shape)
    print(Pr.shape)
    mat = 0.5 * np.abs(Px - Pr)
    print(mat.shape)
    return np.sum(a=mat, axis=1)   # sume pe linii