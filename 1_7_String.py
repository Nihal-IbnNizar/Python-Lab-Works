def check_substring(str1, str2):
    if str1 in str2:
        return True
    else:
        return False

def count_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

def replace_substring(string, old_substring, new_substring):
    return string.replace(old_substring, new_substring)

def convert_to_capital(string):
    return string.upper()

def menu():
    print("Menu:")
    print("1. Check if String is Substring of Another String")
    print("2. Count Occurrences of Character")
    print("3. Replace a Substring with Another Substring")
    print("4. Convert to Capital Letters")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    return choice

while True:
    choice = menu()

    if choice == '1':
        str1 = input("Enter the first string: ")
        str2 = input("Enter the second string: ")
        if check_substring(str1, str2):
            print(f"{str1} is a substring of {str2}")
        else:
            print(f"{str1} is not a substring of {str2}")

    elif choice == '2':
        string = input("Enter the string: ")
        char = input("Enter the character to count: ")
        count = count_occurrences(string, char)
        print(f"The character '{char}' appears {count} times in '{string}'")

    elif choice == '3':
        string = input("Enter the string: ")
        old_substring = input("Enter the substring to replace: ")
        new_substring = input("Enter the new substring: ")
        new_string = replace_substring(string, old_substring, new_substring)
        print(f"Original string: '{string}'")
        print(f"Modified string: '{new_string}'")

    elif choice == '4':
        string = input("Enter the string: ")
        capitalized_string = convert_to_capital(string)
        print(f"The string in capital letters: {capitalized_string}")

    elif choice == '5':
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
