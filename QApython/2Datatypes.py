#tutorial

word1 = "Good"
word2 = "Day"
word3 = "John"
sentence = word1 + " " + word2 + " " + word3
print(sentence)


#exercise - integers and float
number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))


print(number1)
print(number2)
print(round_number)

"""
takes in a number, converts it to a non-decimal int, 
takes in another number, converts it into float (decimal), and then rounds it off  
prints out number1 and number2 initially entered, and rounded number 
(e.g. if entering 7.3 as number2, it becomes 7 at the end. For 7.5 it would be 8)
"""

#exercise - boolean

#pet
name = "Pep Guardogiola"
age = 3
bark = True
tweet = False 

print("My pet is called", name, " He is", age, "years old.")
print("Statement:", name, "barks.", bark)
print("Statement:", name, "tweets.", tweet)

#prints out pet name and age, then prints out whether the dog barks (true), then whether the dog tweets (false)