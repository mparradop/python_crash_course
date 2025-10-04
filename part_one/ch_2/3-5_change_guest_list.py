"""
Changing guest list:
-Start w/ your program from 3-4. Add a print() call at the end of your program, stating the name of the guest who can't make it
-Modify your list, replacing the name of the guest who can't make it w/ the name of the person you're inviting
-Print a second set of invitations messages, one for each person who is still in your list.
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
