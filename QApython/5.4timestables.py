# Write a program that takes a number and prints the full times table of that number. Do not include 0.
# Hint: don’t manually set your code to print each number, one by one. Use a loop.

number = int(input("Number: "))

for i in range(1, number+1):
    for j in range(1, number+1):
        print(f'{i*j:5}', end='')
    print("\n")