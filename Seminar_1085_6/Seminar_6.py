import numpy as np
import Grafice as graf
import pandas as pd


# creati un ndarray (20, 15) de valori aleatoare in virgula mobila
# in intervalul [1, 10)
nda_1 = np.random.uniform(low=1, high=10, size=(20, 15))
print(nda_1, type(nda_1))
# calculati matrice de corelatie, coeficent de corelatie Pearson
# avem variabilele pe coloane
corr = np.corrcoef(x=nda_1, rowvar=False)  # avem variabilele pe coloane
print(corr)

# apel corelograma din numpy.ndarray
# graf.corelograma(corr, dec=1)
# graf.afisare()

# apel de corelograma cu pandas.DataFrame
corr_df = pd.DataFrame(data=corr,
            index=('V'+str(i+1) for i in range(corr.shape[0])),
            columns=('V'+str(j+1) for j in range(corr.shape[1])))
print(corr_df, type(corr_df))
# graf.corelograma(corr_df, titlu='Corelograma din pandas.DataFrame')
# graf.afisare()

# apel cercul corelatiilor
graf.cercul_corelatiilor(R2=corr)
# apel cercul corelatiilor din pandas.DataFrame
graf.cercul_corelatiilor(R2=corr_df,
                titlu='Cercul corelatiilor din pandas.DataFrame')
# apel cu un tip de data invalid
# graf.cercul_corelatiilor(R2='mama')
# graf.afisare()

# generati un vector de 12 valori aleatoare in [0.5, 3)
valori_proprii = np.random.uniform(low=0.5, high=3, size=12)
print(valori_proprii, type(valori_proprii), valori_proprii.shape)
# sortare masiv ndarray
valori_proprii = np.sort(a=valori_proprii)
print(valori_proprii)
# inversare ordine elemente vector
print(valori_proprii[::-1])

# apel grafic valori proprii
graf.valori_proprii(valori_proprii[::-1])
graf.afisare()