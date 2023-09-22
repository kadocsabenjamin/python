
try:
    szam1 = int(input("szam1:"))
    szam2 = int(input("szam2:"))

    eredmeny = szam1 / szam2

    print(eredmeny)
except ZeroDivisionError:
    print("hiba 0val osztottál")
except ValueError:
    print("nem számot adtál meg")