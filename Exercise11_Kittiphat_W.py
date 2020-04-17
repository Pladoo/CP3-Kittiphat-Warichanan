numberFloor = int(input("Number of floor :"))
space = " "
for x in range(numberFloor):
    space = (numberFloor - x) * " "
    base = (x+(x+1)) * "*"
    print(space , base)
