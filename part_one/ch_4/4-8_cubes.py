#a number raised to the third power is called a cube. Make a list of the first 10 cubes

cubes=[]
for cube in (range(1,11)):
    result = cube**3
    cubes.append(result)
print(f'The first 10 cubes are:{cubes}')

#another way to get the same result

cubos=[]
for cubo in range(1,11):
    cubos.append(cubo**3)
print(f'Los primeros 10 cubos son:{cubos}')