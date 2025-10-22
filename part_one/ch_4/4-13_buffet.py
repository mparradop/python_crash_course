#a buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
#use a for loop to print each food the restaurant offers. 
#try to modify one of the items and make sure that Python rejects the change
#the restaurant changes its menu, replacing two of the items w/ different foods.
#add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

buffet_options = ('club sandwich', 'cesar salad', 'drumsticks', 'lentil soup', 'rice', 'green salad', 'cheese cake')

#buffet_options[1]='garden salad' #TypeError: 'tuple' object does not support item assignment
print(f'The previous menu was: {buffet_options}')

buffet_options = ('smoked salmon', 'garden salad', 'drumsticks', 'lentil soup', 'rice', 'green salad', 'cheese cake')
print(f'The new menu is: {buffet_options}')