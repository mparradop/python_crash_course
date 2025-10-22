#using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following
#print the message 'the first three items in the list are:. Then use a slice to print the first three items from that program's list

#why the first option (numbers) doesn't keep the items when the list is printed again? Why the second option does print it?
"""
Step-by-step:

Python starts building a list comprehension.

For each numero in the range, it calls print(f'#{numero}').

The function print() always returns None — it only outputs text to the console.

The comprehension collects those return values into a list.
"""


#numbers = [print(f'#{number}') for number in range(1,21,2)]
numeros = [numero for numero in range(1,22,2)]
print(numeros)
primeros_tres_items = numeros[:3]
print(f'The first three items in the list are{primeros_tres_items}')# Then use a slice to print the first three items from that program's list
mid=len(numeros)//2

tres_mitad_lista=numeros[(mid-1):(mid+2)]
print(f'the three numbers from the middle are: {tres_mitad_lista}') # Then use a slice to print the three items in the middle from that program's list

ultimos_tres = numeros[-3:]
print(f'the last three numbers are: {ultimos_tres}')
