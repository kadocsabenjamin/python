


A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
B =[
    [1,2,5],
    [6,1,1],
    [1,2,3]
]
C = []
print(A[2][0])

for sor in range(0,3):
    temp_sor = []
    for oszlop in range(0,3):
        er = 0
        for x in range(0,3):
            er += A[sor][x] * B[x][oszlop]
        temp_sor.append(er)
    C.append(temp_sor)

for sor in range(0,3):
    for oszlop in range(0,3):
        print(C[sor][oszlop],end=",")
    print()