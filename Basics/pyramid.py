# Get the number of levels for the pyramid from the user
n = int(input('Enter the number of levels: '))

# Outer loop to handle the number of levels
for i in range(1, n + 1):
    # Inner loop to handle the number of spaces before the stars
    for j in range(n - i):
        print(' ', end='')
    
    # Inner loop to handle the number of stars
    for k in range(2 * i - 1):
        print('*', end='')
    
    # Move to the next line after printing each level
    print()
