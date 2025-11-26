import pandas as pd
import Functii as f


# citirea fisierelor in pandas.DataFrame
etnii_localitati = pd.read_csv(filepath_or_buffer='./dataIN/Ethnicity.csv',
                               index_col=0)
print(etnii_localitati, type(etnii_localitati))

# citire din fisier XLSX
judete = pd.read_excel(io='./dataIN/CoduriRomania.xlsx',
                       sheet_name='Localitati', index_col=0)
print(judete, type(judete))

regiuni = pd.read_excel(io='./dataIN/CoduriRomania.xlsx',
                       sheet_name=1, index_col=0)
print(regiuni, type(regiuni))

macro_regiuni = pd.read_excel(io='./dataIN/CoduriRomania.xlsx',
                       sheet_name=2, index_col=0)
print(macro_regiuni)

merge_judete = etnii_localitati.merge(right=judete,
        left_index=True, right_index=True)
print(merge_judete)

# creare lista nucleu de coloane utila in agregare
etnii = etnii_localitati.columns.values[1:].tolist()
print(etnii, type(etnii))

# creare lista de coloane pentru agregarea la nivel de judet
coloane_judet = etnii + ['County']
print(coloane_judet, type(coloane_judet))

# agregam pe baza judetului
agregare_judet = merge_judete[coloane_judet].groupby(by='County').sum()
print(agregare_judet, type(agregare_judet))

# salvare in fisier CSV
agregare_judet.to_csv('./dataOUT/EtniiJudete.csv')

# agregare la nivel de regiune
merge_regiuni = agregare_judet.merge(right=regiuni,
        left_index=True, right_index=True)
print(merge_regiuni)

coloane_regiune = etnii + ['Regiune']
print(coloane_regiune, type(coloane_regiune))

agregare_regiune = merge_regiuni[coloane_regiune].groupby(by='Regiune').sum()
print(agregare_regiune, type(agregare_regiune))
# salvare agreagare la nivel de regiuni in fisier CSV
# TODO

# apel indice de disimilaritate
indice_disim = f.indice_disimilaritate(table=etnii_localitati, cols=etnii)
print(indice_disim, indice_disim.shape)

