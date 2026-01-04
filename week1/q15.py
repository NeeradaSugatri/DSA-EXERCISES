numbers = [12, 45, 3, 98, 7, 34, 21]

#a)print all numbers
print("All numbers")
for num in numbers:
    print(num)

#b)print only numbers greater than 30
print("\n Numbers greater than 30: ")
for num in numbers:
    if num>30:
        print(num)

#c)count how many numbers are greater than 30
count = 0
for num in numbers:
    if num > 30:
        count += 1
print("\n Count of numbers greater than 30:",count)

