# ISBN's (International Standard Book Numbers) are identifiers for books.
# The ISBN is a thirteen-digit code.
# The last digit is a check number calculated as follows:


# The first 12 digits are taken
# Starting at index 0, if the index is even - add it, and if the index is odd – multiply the digit by three then add it.


# From the sum find the remainder after dividing by 10.
# 10 minus the remainder give us the check digit


# In other words the following algebra would give us the check digit:
# digit_12 = 10 – (( digit_0 + (3 x digit_1) + digit_2 + (3 x digit_3) + digit_4 + (3 x digit_5) + digit_6 + (3 x digit_7) + digit_8 + (3 x digit_9) + digit_10 + (3 x digit_11) ) % 10)


# For ISBN:
# 978-0-306-40615-?
# Would give:
# 978-0-306-40615-7

# isbn = '978-0-306-40615-?'
isbn = '978186197271'
sumlist = []

def cleanisbnlist(list):
    cleanedlist = []
    for i in list:
        try:
         if isinstance(int(i), int):
             cleanedlist.append(int(i))
        except:
            pass
    return cleanedlist

for index, number in enumerate(cleanisbnlist(isbn), start=0):
    if index % 2 == 0:
        sumlist.append(number)
    else:
        sumlist.append(number*3)

print(10-(sum(sumlist)%10))



#978030640615

#(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12) = isbn[0], isbn[1], isbn[2], isbn[4], isbn[6], isbn[6], isbn[7], isbn[8], isbn[10],
#isbn[11], isbn[12], isbn[13], isbn[14]


# digit_12 = 10 - (( 
# int(isbn[0]) + 
# (3*int(isbn[1])) + 
# int(isbn[2]) + 
# (3*int(isbn[1])) + 
# int(isbn[2]) + 
# (3*int(isbn[1])) + 
# int(isbn[0]) + 
# (3*int(isbn[1])) + 
# int(isbn[2]) + 
# (3*int(isbn[1])) + 
# int(isbn[0])) + 
# (3*int(isbn[1])) % 10)


# def numbercheckisbn(number):
#         return number*3

# def cleanisbnlist(list):
#     cleanedlist = []
#     for i in list:
#         try:
#          if isinstance(int(i), int):
#              cleanedlist.append(int(i))
#         except:
#             pass
#     return cleanedlist

# def calculatechecknumber(cleanedlist):
#     total = 0 
#     oddevenlist = []
#     for number, index in enumerate(cleanedlist, start=0):
#         print(number, index)
#         if index == 0 or index % 2 == 0:
#             oddevenlist.append(number)
#         else:
#             oddevenlist.append(numbercheckisbn(number))
#     print(oddevenlist)
#     print(10-(sum(oddevenlist)%10))