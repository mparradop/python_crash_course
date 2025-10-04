"""
Changing guest list:
-Start w/ 3-5, add a print* call to the end of your program, informing people that you found a bigger table
-use insert() to add one new guest to the beginning of your list
-use insert() to add one new guest to the middle of your list
-use append() to add one new guest to the end of your list
"""

guests=['Lucy','Ale','Vero','Rafael', 'Gabriel', 'Erika', 'Gustavo', 'Guillermo']

for guest in guests:
    print(f'Hi {guest}: This invitation is valid for a dinner someday')

#confirm the list 
print(f'This is the initial list of guests:\n{guests}')

#modify your list
declined_guest='Erika'

#what if the new guest should use the free spot?
list_spot=guests.index(declined_guest) #now we know the spot number.

guests.remove(declined_guest)
print(f'{declined_guest} has declined the invitation')

print(guests)

#include a new guest
new_guest = 'Oscar'  
#OPTIONAL guests.append(new_guest)#this line would add the new guest at the end of the list.
guests.insert(list_spot, new_guest)
print(f'{new_guest} has been added to the guest list')

#confirm the new list
print(f'This is the new list of guests:\n{guests}')

print('Hey!, good news, a bigger table has been found!')
new_guest='Diana'
guests.insert(0,new_guest)#new guest at the beginning of the list
print(f'{new_guest} has been added at the beginning of the list')

#new guest at the middle of the list
#how long is the list??
current_lenght=len(guests)
print(f'Number of guests so far: {current_lenght}')
new_guest = 'Alvaro'
if current_lenght%2==0:
    middle_index=(current_lenght/2)-1#consider that the index list starts at 0, so it is
else:
    middle_index=(current_lenght/2)#consider that the index list starts at 0, so it is
guests.insert(int(middle_index), new_guest)
print(f'{new_guest} has been added at the middle of the list')
print(f'New list of guests:\n{guests}')
new_guest='Leo'
guests.append(new_guest)
print(f'{new_guest} has been added at the middle of the list')

for guest in guests:
    print(f'Hi {guest}: This invitation is valid for a dinner someday')