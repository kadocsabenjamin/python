
#      *
#     ***
#    *****
#   *******
#  *********
# ***********


n = int(input("n= "))

spaces = " " * (n - 1)
stars = "*"

for i in range(1,n+1):
   print (spaces + stars)
   spaces = " " * (n - 1 - i)
   stars += "**"
