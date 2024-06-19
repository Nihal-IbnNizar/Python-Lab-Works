def palindrome(n):
    original = n
    reversed_number = 0
    
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n // 10             # // is used to round the result to the nearest
    
    return original == reversed_number

def rev_add_until_palindrome(n):
    while not palindrome(n):
        reversed_n = reverse_number(n)
        n = n + reversed_n
    return n

def reverse_number(n):
    reversed_number = 0
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n // 10
    return reversed_number

number = int(input("Enter a number: "))

result = rev_add_until_palindrome(number)

print("The palindrome obtained is: ",result)
