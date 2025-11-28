

id_lucy= '10lp60'
id_guillo= '09gp53'

flavor='orange'
fruit='ORANGE'

height_lucy=160
height_guillo=159

pizza_toppings = ['peperonni','mushrooms','pineapple','ham']


#test for equality
is_Equal = False

if id_lucy==id_guillo:
    is_Equal=True
else:
    is_Equal= False
print(f'The test result is: {str(is_Equal)}')

#test using the lower() method
if flavor==fruit.lower():
    is_Equal=True
else:
    is_Equal=False
print(f'The test result is: {str(is_Equal)}')

#test using the 'and' keyword
if height_guillo < height_lucy and flavor == "orange":
    print(f'The two conditions were met')
else:
    print(f'One condition is false')

#test whether an item is in a list
topping = 'cheese'
if topping in pizza_toppings:
    print(f'{topping} is on the list')
else:
    print(f'{topping} is not on the list')