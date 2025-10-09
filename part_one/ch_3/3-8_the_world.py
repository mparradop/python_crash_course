locations=['Argentina', 'Spain', 'Germany', 'Colombia', 'UK']
print(f'1. Original order of the list: {locations}')#print your list in its original order.

#use sorted() to print your list in alphabetical order w/o modifying it.
print(sorted(locations))

#show that your list is still in its original order
print(f'2. Original order of the list: {locations}')

#use sorted() to print your list in alphabetical order (reverse).
print(sorted(locations, reverse=True))
print(f'3. Original order of the list: {locations}')

#use reverse() to change the order of your list and print.
locations.sort(reverse=True)
print(f'4. New order of the list (reverse): {locations}')

#use reverse() to put it back to the original order.
locations.sort(reverse=True)
print(f'5. List reordered (reverse): {locations}')
