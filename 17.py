
def fib(x):
    
    print(x)

    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)




#for i in range(0,11):

eredm = fib(5)
print(eredm)
