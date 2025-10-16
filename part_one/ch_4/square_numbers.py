squares=[]
for value in range(1,11):
    square= value **2
    squares.append(square)
print(squares)

#to write this code more concisely, omit the temporary variable square and append each new value directly to the list:

squares_2=[]
for value in range(20,31):
    squares_2.append(value**2)
print(squares_2)


#list comprehension allows you to generate this same list in just one line of code. 
#combines the for loop and the creation of new elements into one line, and automatically appends each new element

squares_3 = [value**2 for value in range(30,41)] #list comprehension
print(squares_3)