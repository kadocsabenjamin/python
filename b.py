

szamlalo = 3
szamlalo_e = 3
oszto = 2

counter = 0
for x in range(0,1000):
    szamlalo += 2*oszto 
    oszto += szamlalo_e
    szamlalo_e = szamlalo
    if len(str(szamlalo)) > len(str(oszto)):
        counter += 1




print(counter)