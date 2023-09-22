a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a + b <= c or b + c <= a or a + c <= b:
    print("nem alkotható háromszög")
else:
    print("alkotható háromszög")