#think of at least three kinds of your favorite pizza. Store these pizza names in a list, 
# and then use a for loop to print the name of each pizza.

pizzas = ['hawaian', 'burrata', 'pepperoni', 'four cheese']

for pizza in pizzas:
    print(f'A {pizza.title()} has been added to the order')

print(f'A total of {len(pizzas)} pizzas were ordered') #add a line at the end of your program, outside the for loop

#start w/ the program from exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then do the following

friend_pizzas = pizzas[:]
#add a different pizza to the list friend_pizzas
friend_pizzas.append('mexican')
print(f'My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print(f"My friend's favorite pizzas are:")
for their_pizza in friend_pizzas:
    print(their_pizza)