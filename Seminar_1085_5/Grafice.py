import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd


def corelograma(R2=None, dec=2, titlu='Corelograma',
                valMin=-1,
                valMax=1):
    plt.figure(num=titlu, figsize=(8, 6))
    plt.title(label=titlu, fontsize=12, color='Blue',
              verticalalignment = 'bottom')
    sb.heatmap(data=np.round(R2, decimals=dec),
               vmin=valMin, vmax=valMax, cmap='bwr',
               annot=True)


def cercul_corelatiilor(R2=None, v1=0, v2=1,
                        titlu='Cercul corelatiilor'):
    plt.figure(num=titlu, figsize=(7, 7))
    plt.title(label=titlu, fontsize=12, color='Blue',
              verticalalignment='bottom')
    # desenare cerc de raza 1
    theta = [t for t in np.arange(start=0, stop=2*np.pi, step=0.01)]
    x = [np.cos(t) for t in theta]
    y = [np.sin(t) for t in theta]
    plt.plot(x, y)
    plt.axhline(y=0, c='Green')
    plt.axvline(x=0, c='Green')

    # if isinstance(R2, np.ndarray):
    #     # TODO
    # elif isinstance(R2, pd.DataFrame):
    #     # TODO
    # else:
    #     print('Tip de data necunoscut!')


def afisare():
    plt.show()