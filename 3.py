city_country = (("Budapest", "Magyarország"),("Berlin","Németország"),("Párizs", "Franciaország"))

city = input("add meg a várost: ")

print(len(city_country))

found = None
for x,y in city_country:
    if city == x:
        found = y
        break

if found:
    print("a ", city, "-hez tartozó ország az a: ", found)