txt = open("sudoku.txt", "r")

sudoku = []
sudoku_halmaz = []
for sor in txt:
    if sor[0] == "G":
        sudoku_halmaz.append(sudoku)
        sudoku = []
    else:
        sudoku.append(sor)

for x in sudoku_halmaz:
    print(x)
txt.close()