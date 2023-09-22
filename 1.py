# Készíts egy programot, amely bekéri a felhasználó nevét és életkorát. Ezután írd ki a 
# képernyőre üdvözlő üzenetet, amely tartalmazza a felhasználó nevét és azt az évet amikor született

name = input("add meg a nevedet: ")
age = int(input("add meg a korod: "))

born = 2023 - age

print("neved: ", name)
print("született: ", born)



