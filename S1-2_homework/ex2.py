import numpy as np


def coloane_cu_minim_egal_cu_5(matrice):
    coloane_selectate = []

    for i in range(matrice.shape[1]):
        coloana=matrice[:,i]
        if np.min(coloana) == 5:
            coloane_selectate.append(coloana)

    return coloane_selectate
matrice = np.array([[1,5,3,4],
                    [3,6,9,2],
                    [4,7,2,1]])
rezultat=coloane_cu_minim_egal_cu_5(matrice)
for col in rezultat:
    print(col)