map = [
    'XOOO',
    'XOXO',
    'XOXO',
    'OOXX',
    'OOOO'
 ]
s = ""
for i in range(0,len(map[0])):
    s += "O"
map.insert(0,s)
map.append(s)

for sor in range(0,len(map)):
    map[sor] = "O" + map[sor] + "O"

szam_tomb = []
for sor in range(0,len(map)):
    szam_tomb_sor = []
    for oszlop in range(0,len(map[sor])):
        szam_tomb_sor.append(0)
    szam_tomb.append(szam_tomb_sor)
    
ered = 0
for sor in range(1,len(map)-1):
    for oszlop in range(1,len(map[sor])-1):
        if map[sor][oszlop] == "X":
            counter = 0
            if map[sor-1][oszlop] != "X":
                counter += 1
            if map[sor+1][oszlop] != "X":
                counter += 1
            if map[sor][oszlop-1] != "X":
                counter += 1
            if map[sor][oszlop+1] != "X":
                counter += 1
            szam_tomb[sor][oszlop] = counter
            ered += counter

print(ered)