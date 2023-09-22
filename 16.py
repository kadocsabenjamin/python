class Coor:
    def __init__(self, a, b):
        self.x = a
        self.y = b
        
    
    def kiiras(self):
        print(self.x, self.y)
    

a = 1
b = 5

c = Coor(a, b)
c.kiiras()


duplatomb = [[1,2],[3,4],[5,6,7,8]]

for belsotomb in duplatomb:
    for szamok in belsotomb:
        print(szamok)