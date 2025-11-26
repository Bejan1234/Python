def interschimb(a, b):
    print(a, 'la intrare in functie', id(a))
    print(b, 'la intrare in functie', id(b))
    aux = a
    a = b
    b = aux
    print(a, 'la iesire din functie', id(a))
    print(b, 'la iesire din functie', id(b))
    return None

def interschimb_2(ceva):
    ceva[0], ceva[1] = ceva[1], ceva[0]
    return None

