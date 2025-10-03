import random
operatiors = ['+','-','*','/']

a=0
b=0

for operator in operatiors:
    output = int(a + operator + b)
    while output != 8:
        a,b = random.randint(1,50)
        print(f'a={a}, b={b}')
        print(f'The result is: {output}')
