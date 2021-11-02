#tutorial

from typing import final


def add_calc(number1, number2):
    answer = number1 + number2
    return answer 

added_number = add_calc(5, 5)
print(added_number + 20)

#exercise

name = input("Type in your name: ")
homeworkscore = int(input("Type in your homework score (/25): "))
assessmentscore = int(input("Type in your assessment score (/50): "))
finalexamscore = int(input("Type in your final exam score (/100): "))


def workoutgrade(name, homeworkscore, assessmentscore, finalexamscore):
    ICTgrade=""
    percentage = homeworkscore + assessmentscore + finalexamscore / 175
    if percentage > 50:
        ICTgrade='pass'
        return name, round(percentage, 2), ICTgrade
    elif percentage > 60:
        ICTgrade='B'
        return name, round(percentage, 2), ICTgrade
    elif percentage > 70:
        ICTgrade='A'
        return name, round(percentage, 2), ICTgrade
    else:
        ICTgrade='failed'
        return name, round(percentage, 2), ICTgrade

x = print(workoutgrade("squid", 20, 40, 80))
y = print(workoutgrade("hassan", 25, 50, 100))
z = print(workoutgrade("john", 15, 20, 50))
q = print(workoutgrade(name, homeworkscore, assessmentscore, finalexamscore))
