import Functii as fun
import matplotlib.pyplot as plt


# pasarea parametrilor la functii in Python
a = 7
b = 11
print(a, id(a))
print(b, id(b))
fun.interschimb(a, b)
print(a, id(a))
print(b, id(b))

# in Python parametrui la functii sunt pasati ca referinte
# la obiecte

vector = [7, 11]  # este o lista cu 2 valori numerice
print(vector, type(vector))
fun.interschimb_2(vector)
print(vector, type(vector))

# list comprehension
# posibilitatea de a intializa si popula liste cu
# obiecte in mod programatic
list_1 = ['mama', 3.14, 3, [1, 2, 3]]
print(list_1)
list_2 = [x for x in list_1]  # deep copy
print(list_2, type(list_2))

# creati o lista care sa contina primele 100 de numere naturale
# de la 1 la 100
list_3 = [x for x in range(1, 101, 1)]
# range(inceput, final, pas)
# inceput este implicit zero
# si pasul este implicit 1
# funrnizeaza un interval de valori intregi deschis la dreapta
print(list_3)
list_4 = [(x+1) for x in range(100)]
# mergem pentru f(x) = x+1 , cu x in [0,99]
print(list_4)

# putem implementa o functie de una sau mai multe variabile
# creati lista cuburilor primelor 100 de numere naturale
# de la 1 la 100
list_5 = [(x+1)**3 for x in range(100)]
print(list_5)
# plt.plot(list_5)  # grafic de puncte unite cu segmente de aceeasi grosime
# plt.show()

# comprehension de 2 variabile
list_6 = [2, 4]
list_7 = [(x+y)**2 for x in list_6
          for y in list_4]
print(list_7)
print(len(list_7))  # obtinem produsul cartezian al celor 2 multimi
# de valori

# dictionare in Python
# colectii asociative de perechi (cheie, valoare)
# cheia trebuie sa fie de timp imuabil sau potetial imuabil
dict_1 = {'luni': 'mama',
          'marti': 3.14,
          'miecuri': [1, 2, [3, 4]]}
print(dict_1, type(dict_1))
# access dupa cheie
print(dict_1['luni'])
# acces la multimea de chei
print(dict_1.keys(), type(dict_1.keys()))
# orice colectie secventiala de obiect epoate fi asimilata
# si convertita la o lista
print(list(dict_1.keys()), type(list(dict_1.keys())))

# acces la colectia de valori
print(dict_1.values(), type(dict_1.values()))
print(list(dict_1.values()), type(list(dict_1.values())))

# putem obtine o colecti de prechi (k, v)
print(dict_1.items(), type(dict_1.items()))
for (k, v) in dict_1.items():
    print(k, ':', v)

# dictionary comprehension
dict_2 = {x: x+1 for x in range(100)}
print(dict_2)
# creati un dictionar cu chei numere intregi in [-10, 10]
# cu valori cuburile acestor numere intregi
dict_2 = {x: x**3 for x in range(-10, 10)}
plt.plot(dict_2.keys(), dict_2.values())
plt.show()

# dictionary comprehension pentru 2 sau mai multe variabile




