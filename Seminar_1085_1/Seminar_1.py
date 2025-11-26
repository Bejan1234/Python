print('Buna din Python!')

# Tutoriale Python
# https://www.w3schools.com/python/
# https://www.tutorialspoint.com/python/index.htm

'''
Acesta
este
un comentariu
extins
pe mai multe
linii
'''

a = 'mama'
print(a, type(a))
a = 5
b = 3
print(a, type(a))

print('Restul impartirii lui 5 la 3:', a % b)
# operatori specifici Python pentru date numerice
print('Catul impartirii lui 5 la 3:', a // b)
print('3 la puterea a 5-a:', b ** a)

str_1 = 'mama mea este frumoasa'
print(str_1, type(str_1))
str_2 = 'mama said: "do not be late!"'
print(str_2, type(str_2))
str_3 = "mama said: don't be late!"
print(str_3, type(str_3))
str_4 = '''mama said: "don't be late"'''
print(str_4, type(str_4))

# String-uri sunt immutable
str_5 = 'mama mea'
print(str_5, id(str_5))
str_5 += ' este ' + 'cea mai buna!'
# operatori supraincarcati pentru ocncatenarea de string-uri
print(str_5, id(str_5))

# liste in Python
list_1 = [1, 3.14, 'mama', [1, 2, 3]]
print(list_1, type(list_1))
list_2 = list_1 + ['si acest text']
print(list_2)

# list slicing
list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_3)
# acces la ultimul element al listei
# listele in Python sunt structuri circulare
print(list_3[-1])
print(list_3[:]) # [inceput : final : pas], interval deschis la dreapta
print(list_3[::])

# listati elementele de pe pozitiile pare ale listei
print(list_3[::2])
# listati elementele de pe pozitiile impare ale listei
print(list_3[1::2])

# inversati ordinea elemnetelor listei
print(list_3[-1::-1])
print(list_3[::-1])

# list comprehension
list_4 = [x for x in list_3]
print(list_4)

