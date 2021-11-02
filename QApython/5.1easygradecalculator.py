# Create an application which asks the user for an input for a maths mark, a chemistry mark and a physics mark.
# Add the marks together, then work out the overall percentage. And print it out to the screen.
# If the percentage is below 40%, print “You failed”
# If the percentage is 40% or higher, print “D”
# If the percentage is 50% or higher, print “C”
# If the percentage is 60% or higher, print “B”
# If the percentage is 70% or higher, print “A”

print("Welcome to grade calculator")
mathsmark = int(input("Please enter in a maths percentage: "))
chemistrymark = int(input("Please enter in a chemistry percentage: "))
physicsmark = int(input("Please enter in a physics mark: "))
totalmark = mathsmark + chemistrymark + physicsmark
averagemark = totalmark/3
print("Your average percentage is: ", averagemark)

if averagemark >= 70:
    print("A")
elif averagemark >= 60:
    print("B")
elif averagemark >= 50:
    print("C")
elif averagemark >= 40:
    print("D")
else:
    print("You failed")