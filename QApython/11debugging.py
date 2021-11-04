#tutorial - visual studio debugging seems better to me 

# import pdb

# a = "aaa"
# b = "bbb"
# c = "ccc"

# def final(var1, var2, var3):
#     return(var1+var2+var3)

# print(final(a,b,c))

#exercise

#example

# def tail_recursion(factorial, result=1):
#     if factorial == 1:
#         return result 
#     else:
#         tempresult = factorial * result
#         return tail_recursion(factorial-1, tempresult)


#static analysis i.e. view code

# price = {'Burger':10}
# user_funds = 10.31
# item_price = price["Burger"]

# if item_price < user_funds:
#     print("You have enough money!")
# if item_price == user_funds:
#     print("You have the precise amount of money")
# if item_price > user_funds:
#     print("Sorry you don't have enough money")

#static analysis 
# 4 4 5 

# def product(n):
#     total = 1
#     for i in n:
#         total = total * i
#     return total 

# print(product([4,4,5]))


#dynamic analysis i.e. use of tools when running 

# def is_prime(x):
#     if x == 1:
#         return False
#     else:
#         for n in range(2, x-1):
#             if x % n == 0:
#                 return False
#         return True

# print(is_prime(7))


#dynamic analysis

# item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
# n = 0

# while n <= 5:
#     for i in range(len(item_list)):
#         print(item_list[i])
#     n = n + 1

# print(item_list[4])