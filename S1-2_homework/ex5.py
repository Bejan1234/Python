def cmmdc(a, b):
    # Cazul de bază: când b devine 0, CMMDC este a
    if b == 0:
        return a
    else:
        # Apel recursiv cu b și restul împărțirii lui a la b
        return cmmdc(b, a % b)


print(cmmdc(56,98))

