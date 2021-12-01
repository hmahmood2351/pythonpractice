# Write a program to:

# find all numbers, between 2000 and 3200 (both included), 
# that are divisible by 7, but are not a multiple of 5

# The numbers obtained should be returned on a single line. 
# seperated by commas.

# numbers = []
# for i in range(2000,3200):
#     if (i%7==0) and (i%5!=0):
#         numbers.append(i)
# print(numbers)

# for index, i in enumerate(numbers):
#     print(i, end=' ')



# Given an integer n, write a python function which returns a
# times table grid for all the integers between 1 and n.
# The grid should be separated by tabs and new lines.

# For example, given n = 4 it should return the grid

# 1   2   3   4
# 2   4   6   8
# 3   6   9   12
# 4   8   12  16

# given n=7 it should return

# 1   2   3   4   5   6   7   
# 2   4   6   8   10  12  14  
# 3   6   9   12  15  18  21  
# 4   8   12  16  20  24  28  
# 5   10  15  20  25  30  35  
# 6   12  18  24  30  36  42  
# 7   14  21  28  35  42  49  

# number = int(input("Enter in times table number: "))
# for i in range(1,number+1):
#     for j in range(1,number+1):           
#         print(f'{j*i:5}', end=' ')
#     print()

# Write a program which will do the following:

# Create a list which contains the first name of everyone in your 
# cohort and store it in a variable called team.

# Add your trainer to the list without manually editing it.

# Print the list to the terminal.

# Print only the 5th person in the list to your terminal.

# Print the number of times Chris occurs in the list team, 
# to the terminal.

# cohort = ['hassan', 'squid', 'beaver', 'cat', 'armadillo']

# cohort.append("Deep")

# print(cohort)

# print(cohort[4])

# print(cohort.count('squid'))

# Write a program which can compute the factorial of a given number.

# The factorial of any given number is the 
# multplication every whole number from our chosen one 
# all the way down to 1.

# So the factorial of 8 is 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 40320

# For example:

# fact(8) ⟶ 40320
# fact(5) ⟶ 120
# fact(4) ⟶ 24 

# factorial = int(input("Type in number to compute factorial from: "))
# result = factorial

# for i in range(1, factorial):
#     result = result * i

# print(result)  

# Define a class named Rectangle, which can be constructed by a length 
# and width.

# The Rectangle class needs to have a method that can compute area.

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width 
    
    def computearea(self):
        return self.length*self.width

rectangle1 = Rectangle(3,10)
print(rectangle1.computearea())