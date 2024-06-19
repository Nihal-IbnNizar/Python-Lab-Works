count = 0
sum = 0

for i in range(101, 200):
    if i % 7 == 0:
        count += 1
        sum += i

print("The number of integers: ",count)
print("The sum of these integers is: ",sum)
