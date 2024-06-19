a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

op = input('Select the operation [+, -, *, / ] :')

if op == '+':
    res = a + b
elif op == '-':
    res = a - b
elif op == '*':
    res = a * b
elif op == '/':
    if b == 0:
        print('Division by zero is not possible')
        res = None
    else:
        res = a / b
else:
    print('Invalid operation')
    res = None

if res is not None:
    print('Result:', res)
