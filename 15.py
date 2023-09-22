# Feladat: Írj egy programot, amely kiszámolja és kiírja az első 20 prímszámot.

def is_prime(szam):
    if szam < 2:
        return False

    for i in range(2, int(szam ** 0.5) + 1):
        if szam % i == 0:
            return False

    return True

primes = []

tesztszam = 2 

while len(primes) < 20:
    if is_prime(tesztszam):
        primes.append(tesztszam)
    tesztszam += 1

print(primes) 






