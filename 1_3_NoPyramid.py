def number_pyramid(n):
    for i in range(1, n + 1):
        for j in range(n - i):              # Print leading spaces
            print(" ", end="")

        for j in range(1, i + 1):           # Print increasing numbers
            print(j, end="")

        for j in range(i - 1, 0, -1):       # Print decreasing numbers
            print(j, end="")

        print()                             # Move to the next line

levels = int(input("Enter the number of levels in the pyramid: "))
number_pyramid(levels)
