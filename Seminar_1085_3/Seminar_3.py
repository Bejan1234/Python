import numpy as np
import Functii as f
import pandas as pd


# dictionary comprehension de 2 sau  mai multe variabile
print([x for x in range(10)])
print((1, 2))
dict_1 = {(x+y): (x+y)*2 for x in range(10) for y in (1, 2)}
print(dict_1)
print(len(dict_1))
# in procesul de creare a dictionarului sunt obtinute chei duplicate si
# valorile asociate lor sunt suprascrise

# daca chiar dorim sa obtinemun produs Cartezian
dict_2 = {(x, y): (x+y)*2 for x in range(10) for y in (1, 2) }
print(dict_2)
print(len(dict_2))

# utilizarea functiei zip(l1, l2, ...)
l_1 = (1, 2, 3, 4, 5, 6)
l_2 = (1, 2, 3)
print(tuple(zip(l_1, l_2)))

dict_3 = {(x+y): (x+y)*2 for (x, y) in tuple(zip(l_1, l_2)) }
print(dict_3)
print(len(dict_3))

# functii generator in Python
# creati un generator care sa produca urmatorul
# numar natural de la 1 la infinit
# extrageti si tipariti primele 10 numere naturale
# apeland generatorul
def generator():
    t = 0
    while True:
        t += 1
        yield t

apel_generator = generator()
for i in range(10):
    try:
        print('Urmatoarea valoare=', next(apel_generator))
    except:
        break

# generati patratele primelor 10 numere naturale de la 1
# folosind un generator
# nu exista comprehension pentru tupluri!
gen_1 = ((x+1)**2 for x in range(10))
print(gen_1, type(gen_1))
for i in range(10):
    try:
        print('Urmatoarea valoare=', next(gen_1))
    except:
        break

# sau ...
for valoare in gen_1:
    print(valoare)

# creati un dictionar care sa aiba 4 chei de forma S1, S2, S3, S4
# iar valorile sunt liste de note de cate 6 valori intregi
# aleatoare in [1, 10]
vector = np.random.rand(6)
print(vector, type(vector))
nda_1 = f.random_AB(1, 11, 6)
print(nda_1, type(nda_1))
dict_4 = {'S'+str(i+1): [x for x in f.random_AB(1, 11, 6)]
          for i in range(4)}
print(dict_4)
for (k, v) in dict_4.items():
    print(k, ':', v)

# creare pandas.DataFrame din dictionar
df_1 = pd.DataFrame(data=dict_4)
print(df_1, type(df_1))

# creati un DataFrame dintr-un masiv cu 2 dimensiuni
# 6 linii si 7 coloane
# continand numere aleatoare in [-5, 5)
# etichete de linii in forma L_1, L-2, ...
# si d ecoloane in forma C_1, C_2, ...
print(np.random.randint(low=-5, high=5, size=(6, 7)))
df_2 = pd.DataFrame(data=np.random.randint(low=-5, high=5, size=(6, 7)),
                    index=('L_'+str(i+1) for i in range(6)),
                    columns=('C_'+str(j+1) for j in range(7)))
print(df_2)





