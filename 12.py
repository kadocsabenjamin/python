

n = 10

a = 0
b = 1

fib = [b]

while len(fib) < n:
    a, b = b, a + b
    fib.append(b)
print(fib)