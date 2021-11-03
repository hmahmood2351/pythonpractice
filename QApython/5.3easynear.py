# Create a function that when given two strings of letters, 
# determine whether the second can be made from the first by removing one letter.
# The remaining letters must stay in the same order.

# def near(str1, str2):

#     # test for right number of letters in strings
#     if len(str1) - len(str2) != 1:
#         return False

#     # remove one letter from string 1 and check if equal to string 2
#     for i in range(len(str1)):
#         s = str1[:i] + str1[i+1:]
#         if s == str2:
#             return True
#     else:
#         return False

# print(near("reset", "rest"))

# print(near("dragoon", "dragon"))

# print(near("eave", "leave"))

# print(near("sleet", "lets"))

def onecharremove(string1, string2):
    for i in string1:
        if string1.replace(i, '', 1) == string2:
            return True
    else:
        return False

x = input("First string: ")
y = input("Second string: ")
z = print(onecharremove(x, y))
