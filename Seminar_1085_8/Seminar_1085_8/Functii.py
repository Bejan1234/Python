import numpy as np


def standardizare(X):
    # asumam ca X este numpy.ndarray
    medii = np.mean(a=X, axis=0) # calculam medii pe coloane
    # avem variabilele pe coloane
    abateri_std = np.std(a=X, axis=0) # avem variabilele pe coloane
    return (X - medii) / abateri_std
