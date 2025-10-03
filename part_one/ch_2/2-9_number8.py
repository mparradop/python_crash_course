import random
operators = ['+','-','*','/']
data = []

a=0
b=0
output=0
iterations = 0
c = random.randint(1,50)

for operation in operators:
    while output != c:
        a = random.randint(1,50)
        b = random.randint(1,50)
        calculation = str(a) + operation + str(b)
        output = eval(calculation)
        #print(f'a={a}, b={b}\t {operation}')
        #print(f'This time the result is: {output}')
        iterations +=1
    
    #print(f'The result is: {output}, it took {iterations} evaluation(s) to get {c}.\nMoving to the next operator...')
    data.append(f'({operation}):{a}{operation}{b}={output}, it took {iterations} evaluation(s) to get {c}.')
    
    output=0
    iterations =0

print(data)


