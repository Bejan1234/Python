import numpy as np


def linii_crescatoare(matrice):


    count = 0


    for linie in matrice:
        # Verificăm dacă linia este în ordine crescătoare
        if all(linie[i] < linie[i + 1] for i in range(len(linie) - 1)):
            count += 1  # Incrementăm contorul dacă linia este crescătoare

    return count



matrice = np.array([[1, 2, 3, 4],
                    [5, 4, 3, 2],
                    [7, 8, 9, 10]])


print("Numărul liniilor cu elemente în ordine crescătoare:", linii_crescatoare(matrice))
