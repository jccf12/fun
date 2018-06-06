def ones_and_twos(n):
    return int(n/2) + 1


def fives(n):
    suma = 0
    for x in range(int(n/5)+1):
        suma += ones_and_twos(n-5*x)
    return suma


def tens(n):
    suma = 0
    for x in range(int(n/10)+1):
        suma += fives(n-10*x)
    return suma


def twenties(n):
    suma = 0
    for x in range(int(n/20)+1):
        suma += tens(n-20*x)
    return suma


def fifties(n):
    suma = 0
    for x in range(int(n/50)+1):
        suma += twenties(n-50*x)
    return suma


def hundreds(n):
    suma = 0
    for x in range(int(n/100)+1):
        suma += fifties(n-100*x)
    return suma


def pounds(n):
    suma = 0
    for x in range(int(n/200)+1):
        suma += hundreds(n-200*x)
    return suma


print(hundreds(200))
