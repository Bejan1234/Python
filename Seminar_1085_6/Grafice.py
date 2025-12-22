import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
from networkx.algorithms.bipartite import color


def corelograma(R2=None, dec=2, titlu='Corelograma',
                valMin=-1,
                valMax=1):
    plt.figure(num=titlu, figsize=(8, 6))
    plt.title(label=titlu, fontsize=12, color='Blue',
              verticalalignment = 'bottom')
    sb.heatmap(data=np.round(R2, decimals=dec),
               vmin=valMin, vmax=valMax, cmap='bwr',
               annot=True)


def cercul_corelatiilor(R2=None, v1=0, v2=1, dec=2,
                    titlu='Cercul corelatiilor'):
    plt.figure(num=titlu, figsize=(8, 7))
    plt.title(label=titlu, fontsize=12, color='Blue',
              verticalalignment='bottom')
    # desenare cerc de raza 1
    theta = [t for t in np.arange(start=0, stop=2*np.pi, step=0.01)]
    x = [np.cos(t) for t in theta]
    y = [np.sin(t) for t in theta]
    plt.plot(x, y)
    plt.axhline(y=0, c='Green')
    plt.axvline(x=0, c='Green')

    if isinstance(R2, np.ndarray):
        plt.xlabel(xlabel='Variabila '+ str(v1+1),
                   fontsize=10, color='Blue',
                  verticalalignment='top')
        plt.ylabel(ylabel='Variabila ' + str(v2 + 1),
                   fontsize=10, color='Blue',
                   verticalalignment='top')
        plt.scatter(x=R2[:, v1], y=R2[:, v2], color='Red')
        for i in range(R2.shape[0]):
            # plt.text(x=R2[i, v1], y=R2[i, v2], s='text')
            plt.text(x=R2[i, v1], y=R2[i, v2], color='Black',
                s='(' + str(np.round(R2[i, v1], decimals=dec)) + ', ' +
                  str(np.round(R2[i, v2], decimals=dec)) + ')')
    elif isinstance(R2, pd.DataFrame):
        plt.xlabel(xlabel=R2.index[v1],
                   fontsize=10, color='Blue',
                   verticalalignment='top')
        plt.ylabel(ylabel=R2.index[v2],
                   fontsize=10, color='Blue',
                   verticalalignment='top')
        # plt.scatter(x=R2.values[:, v1], y=R2.values[:, v2], color='Blue')
        # plt.scatter(x=R2.iloc[:, v1], y=R2.iloc[:, v2], color='Blue')
        plt.scatter(x=R2.iloc[:].iloc[v1], y=R2.iloc[:].iloc[v2], color='Blue')
        for i in range(R2.index.size):
            plt.text(x=R2.iloc[i, v1], y=R2.iloc[i, v2], color='Black',
                s=R2.index[i])
    else:
        raise Exception('Tip de data invalid!')


def valori_proprii(valori, titlu='Componente principale - varianta explicata'):
    plt.figure(num=titlu, figsize=(10, 6))
    plt.title(label=titlu, fontsize=12, color='Blue',
              verticalalignment='bottom')
    plt.xlabel(xlabel='Componenete principale',
               fontsize=10, color='Blue',
               verticalalignment='top')
    plt.ylabel(ylabel='Valori proprii - varianta explicata',
               fontsize=10, color='Blue',
               verticalalignment='bottom')
    componente = ['C'+str(i+1) for i in range(len(valori))]
    plt.plot(componente, valori, 'bo-')
    # plt.plot(valori, 'b>-')
    # plt.plot(valori, 'b*-')
    # plt.plot(valori, 'b^-')
    plt.axhline(y=1, color='Red')


def afisare():
    plt.show()