factorial_dict = {}

def factorial(n):
    if n < 0:
        return None 
    elif n == 0 or n == 1:
        return 1
    else:
        if n in factorial_dict:
            return factorial_dict[n]
        else:
            result = n * factorial(n - 1)
            factorial_dict[n] = result
            return result

num = 5
print(f"The factorial of {num} is: {factorial(num)}")
print("Factorial dictionary after calculation: ",factorial_dict)
