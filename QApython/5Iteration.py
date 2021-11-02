# tutorial main branch

count = 0 
name = str(input("What is your name? "))

while count < 5:
    print(name, "is awesome!")
    count += 1

for i in range(5, 11):
    print(i)
    
# exercise branch

namelist = []
while True:
    name = input("What is your name?")
    namelist.append(name)
    print(name, "is awesome!")

    if len(namelist) == 5:
        break

# for i in range(5): #asks for 5 names and prints them out with awesome following it 
#     name = input("What is your name? ")
#     print(name, "is awesome!")

# for i in range (10, 21, 2): # prints out even numbers from 10 to 20
#     print(i)