
def primszame(szam):
    #rossz e a szam
    if szam <= 1:
        return False
    #prim e, korabbi feladatbol masolt :(
    for i in range(2, int(szam ** 0.5) + 1):
        if szam % i == 0:
            return False
    return True

def kettesprim(szam):
    for i in range(szam):
        if primszame(i) and primszame(i + 2):
            return i, i + 2
    return None
#nem tudom miért nem a 60. mükodik
print(kettesprim(60))