products = {
    "alma" : 100, 
    "banán": 120, 
    "szőlő": 650
    }

product = input("add meg a terméket: ")

if product in products:
    price = products[product]
    print(f"{product} ára: {price} Forint")

