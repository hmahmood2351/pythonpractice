#Tutorial - committed to main initially

devs_money = 100
dev_can_play_smash = False

if devs_money > 10 and dev_can_play_smash:
    print("Devs can enter a smash tournament")
elif devs_money < 10 and dev_can_play_smash:
    print("Dev is too poor to enter")
else:
    print("Dev can't play smash")

#exercise branch commit - to be merged with main

mark = int(input("Type in your mark: "))
if mark > 85:
    print("Distinction")
elif mark > 65 and mark < 85:
    print("Pass")
else:
    print("Fail")

#without elif

if mark > 85:
    print("Distinction")
else:
    if mark > 65 and mark < 85:
        print("Pass")
    else:
        print("Fail")