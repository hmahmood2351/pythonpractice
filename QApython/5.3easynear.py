# Create a function that when given two strings of letters, 
# determine whether the second can be made from the first by removing one letter.
# The remaining letters must stay in the same order.

def onecharremove(string1, string2):
    for i in string1:
        if string1.replace(i, '', 1) == string2:
            return True
    else:
        return False

x = input("First string: ")
y = input("Second string: ")
z = print(onecharremove(x, y))
