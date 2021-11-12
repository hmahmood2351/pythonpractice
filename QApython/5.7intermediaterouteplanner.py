# You will be given a list of integers, they will be the height of a peak from ground level (1 = 100m). The peaks will appear in a single line as you travel from point A to B.
# Rules:
# You don’t have to climb every peak. But you want to climb as many peaks as possible
# You only want to increase your altitude as going up and down would be too exhaustive.
# There is no going backwards.
# There can be more than one possible output.

# Enter your peaks:
# 0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15
# Best Route: 0 2 6 9 11 15

def returnlistafternumber(list, number):
    counter = 1
    for i in list:
        if i == number:
            return list[counter:]
        counter = counter + 1

peaks = []
solution = []
currentlowestnumber = 0 

while True:
    userpeak = input("Enter in a peak, type 'exit' to exit: ")
    
    if userpeak == 'exit':
        break
    
    peaks.append(int(userpeak))

maxlist = max(peaks)
minlist = min(peaks)
lengthpeaks = len(peaks)
quarterpeaks, halfpeaks, thirdquarterpeaks = len(peaks)//4, len(peaks)//2, (len(peaks)//4)*3
quarterlist, halflist, thirdquarterlist, restlist = peaks[:quarterpeaks], peaks[quarterpeaks:halfpeaks], peaks[halfpeaks:thirdquarterpeaks], peaks[thirdquarterpeaks:] 

print("Maximum of the list is:", maxlist)
print("Minimum of the list is:", minlist)
print("List is", lengthpeaks, "in length")
print("List is: ", peaks)

print("Quarter of the list is: ", quarterlist)
print("Half of the list is: ", halflist)
print("Three quarters of the list is: ", thirdquarterlist)
print("The rest/from three quarters to end is: ", restlist)

if lengthpeaks < 4:
    print("Less than 4 length code executed")




else:
    print("Greater or equal to 4 length of list code executed")

    #iterating through first quarter and finding lowest number
    #checking if there are numbers after the lowest number. if higher than previous (lowest first) number,
    #and next number is in the first half of the list, if not use second lowest number if in first half,
    #if no lowest number in first half, use the lowest in second half of the list 
    #add lowest number and next number(s) to a list of peaks traversed, last number traversed is the lowest number 

    #iterating through second quarter, searching for lowest increase to the last number chosen in peaks traversed list, 
    #same logic applied before here

    #logic applied for third quarter and rest of the list 
    #peaks traversed returned to the user 

    #first quarter first half 

    halfquarterlist, secondhalfquarterlist = quarterlist[:len(quarterlist)//2], quarterlist[len(quarterlist)//2:]
    lowesthalfquarterlist, lowestsecondhalfquarterlist = min(halfquarterlist), min(secondhalfquarterlist)

    for i in quarterlist:
        print(i, end='')
    print()

    #checking if there's numbers after minimum number in firstquarterhalf

    print("First half of the quarter list: ", halfquarterlist)
    print("Lowest number in first half of quarter list is :", lowesthalfquarterlist)

    firstquarterfirsthalflistminnumber = returnlistafternumber(halfquarterlist, lowesthalfquarterlist)
    print(firstquarterfirsthalflistminnumber)


    if len(firstquarterfirsthalflistminnumber) >= 1:
        print("There's numbers after the minimum")
        currentlowestnumber = lowesthalfquarterlist
        solution.append(lowesthalfquarterlist)
        for i in firstquarterfirsthalflistminnumber:
            if i >= currentlowestnumber and i-currentlowestnumber <= currentlowestnumber:
                print("Appending number to solution", i)
                solution.append(i)
                currentlowestnumber = i

    else:
        print("Adding minimum number of first half quarter list to solution.")
        currentlowestnumber = lowesthalfquarterlist
        solution.append(lowesthalfquarterlist)

    print("Numbers after the lowest number in first half of quarter list are", firstquarterfirsthalflistminnumber)

    #first quarter second half 

    print("Second half of the quarter list: ", secondhalfquarterlist)
    print("Lowest number in second half of quarter list is :", lowestsecondhalfquarterlist)


    firstquartersecondhalflistminnumber = returnlistafternumber(secondhalfquarterlist, lowestsecondhalfquarterlist)
    print(firstquartersecondhalflistminnumber)
    if len(firstquartersecondhalflistminnumber) >= 1:
        print("There's numbers after the minimum")
        currentlowestnumber = lowestsecondhalfquarterlist
        solution.append(lowestsecondhalfquarterlist)
        for i in firstquartersecondhalflistminnumber:
            if i >= currentlowestnumber and i-currentlowestnumber <= currentlowestnumber:
                print("Appending number to solution", i)
                solution.append(i)
                currentlowestnumber = i

    else:
        print("Adding minimum number of second half quarter list to solution.")
        currentlowestnumber = lowestsecondhalfquarterlist
        solution.append(lowestsecondhalfquarterlist)

    print("Numbers after the lowest number in second half of quarter list are", firstquartersecondhalflistminnumber)


    #second quarter first half

    halfhalflist, secondhalfhalflist = halflist[:len(quarterlist)//2], halflist[len(quarterlist)//2:]
    lowesthalfhalflist, lowestsecondhalfhalflist = min(halfhalflist), min(secondhalfhalflist)


    for i in halflist:
        print(i, end='')
    print()

    print("First half of the half list: ", halfhalflist)
    print("Lowest number in first half of half list is :", lowesthalfhalflist)

    secondquarterfirsthalflistminnumber = returnlistafternumber(halfhalflist, lowesthalfhalflist)
    print(secondquarterfirsthalflistminnumber)


    if len(secondquarterfirsthalflistminnumber) >= 1:
        print("There's numbers after the minimum")
        currentlowestnumber = lowesthalfhalflist
        solution.append(lowesthalfhalflist)
        for i in secondquarterfirsthalflistminnumber:
            if i >= currentlowestnumber and i-currentlowestnumber <= currentlowestnumber:
                print("Appending number to solution", i)
                solution.append(i)
                currentlowestnumber = i

    else:
        print("Adding minimum number of first half quarter list to solution.")
        currentlowestnumber = lowesthalfhalflist
        solution.append(lowesthalfhalflist)

    print("Numbers after the lowest number in first half of second half list are", secondquarterfirsthalflistminnumber)

    #second quarter second half


    print("Second half of the half list: ", secondhalfhalflist)
    print("Lowest number in second half of half list is :", lowestsecondhalfhalflist)

    secondquartersecondhalflistminnumber = returnlistafternumber(secondhalfhalflist, lowestsecondhalfhalflist)
    print(secondquartersecondhalflistminnumber)


    if len(secondquartersecondhalflistminnumber) >= 1:
        print("There's numbers after the minimum")
        currentlowestnumber = lowestsecondhalfhalflist
        solution.append(lowestsecondhalfhalflist)
        for i in secondquartersecondhalflistminnumber:
            if i >= currentlowestnumber and i-currentlowestnumber <= currentlowestnumber:
                print("Appending number to solution", i)
                solution.append(i)
                currentlowestnumber = i

    else:
        print("Adding minimum number of first half quarter list to solution.")
        currentlowestnumber = lowestsecondhalfhalflist
        solution.append(lowestsecondhalfhalflist)

    print("Numbers after the lowest number in second half of second half list are", secondquartersecondhalflistminnumber)


    #third quarter first half

    halfthirdquarterlist, secondhalfthirdquarterlist = thirdquarterlist[:len(quarterlist)//2], thirdquarterlist[len(quarterlist)//2:]
    lowesthalfthirdquarterlist, lowestsecondhalfthirdquarterlist = min(halfthirdquarterlist), min(secondhalfthirdquarterlist)



    for i in thirdquarterlist:
        print(i, end='')
    print()

    print("First half of the three quarters list: ", halfthirdquarterlist)
    print("Lowest number in first half of third quarter list is :", lowesthalfthirdquarterlist)


    thirdquarterfirsthalflistminnumber = returnlistafternumber(halfthirdquarterlist, lowesthalfthirdquarterlist)
    print(thirdquarterfirsthalflistminnumber)


    if len(thirdquarterfirsthalflistminnumber) >= 1:
        print("There's numbers after the minimum")
        currentlowestnumber = lowesthalfthirdquarterlist
        solution.append(lowesthalfthirdquarterlist)
        for i in thirdquarterfirsthalflistminnumber:
            if i >= currentlowestnumber and i-currentlowestnumber <= currentlowestnumber:
                print("Appending number to solution", i)
                solution.append(i)
                currentlowestnumber = i

    else:
        print("Adding minimum number of first half quarter list to solution.")
        currentlowestnumber = lowesthalfthirdquarterlist
        solution.append(lowesthalfthirdquarterlist)

    print("Numbers after the lowest number in first half of third quarter list are", thirdquarterfirsthalflistminnumber)


    #third quarter second half

    print("Second half of the three quarter list: ", secondhalfthirdquarterlist)
    print("Lowest number in second half of third quarter list is :", lowestsecondhalfthirdquarterlist)

    thirdquartersecondhalflistminnumber = returnlistafternumber(secondhalfthirdquarterlist, lowestsecondhalfthirdquarterlist)
    print(thirdquartersecondhalflistminnumber)


    if len(thirdquartersecondhalflistminnumber) >= 1:
        print("There's numbers after the minimum")
        currentlowestnumber = lowestsecondhalfthirdquarterlist
        solution.append(lowestsecondhalfthirdquarterlist)
        for i in thirdquartersecondhalflistminnumber:
            if i >= currentlowestnumber and i-currentlowestnumber <= currentlowestnumber:
                print("Appending number to solution", i)
                solution.append(i)
                currentlowestnumber = i

    else:
        print("Adding minimum number of first half quarter list to solution.")
        currentlowestnumber = lowestsecondhalfthirdquarterlist
        solution.append(lowestsecondhalfthirdquarterlist)

    print("Numbers after the lowest number in second half of third quarter list are", thirdquartersecondhalflistminnumber)


    #last quarter first half

    halfrestlist, secondhalfrestlist = restlist[:len(quarterlist)//2], restlist[len(quarterlist)//2:]
    lowesthalfrestlist, lowestsecondhalfrestlist = min(halfrestlist), min(secondhalfrestlist)

    for i in restlist:
        print(i, end='')
    print()

    print("First half of the rest list: ", halfrestlist)
    print("Lowest number in first half of rest list is :", lowesthalfrestlist)


    finalfirsthalflistminnumber = returnlistafternumber(halfrestlist, lowesthalfrestlist)
    print(finalfirsthalflistminnumber)


    if len(finalfirsthalflistminnumber) >= 1:
        print("There's numbers after the minimum")
        currentlowestnumber = lowesthalfrestlist
        solution.append(lowesthalfrestlist)
        for i in finalfirsthalflistminnumber:
            if i >= currentlowestnumber and i-currentlowestnumber <= currentlowestnumber:
                print("Appending number to solution", i)
                solution.append(i)
                currentlowestnumber = i

    else:
        print("Adding minimum number of first half quarter list to solution.")
        currentlowestnumber = lowesthalfrestlist
        solution.append(lowesthalfrestlist)

    print("Numbers after the lowest number in first half of final list are", finalfirsthalflistminnumber)



    #last quarter second half

    print("Second half of the rest list: ", secondhalfrestlist)
    print("Lowest number in second half of rest list is :", lowestsecondhalfrestlist)

    finalsecondhalflistminnumber = returnlistafternumber(secondhalfrestlist, lowestsecondhalfrestlist)
    print(finalsecondhalflistminnumber)


    if len(finalsecondhalflistminnumber) >= 1:
        print("There's numbers after the minimum")
        currentlowestnumber = lowestsecondhalfrestlist
        solution.append(lowestsecondhalfrestlist)
        for i in finalsecondhalflistminnumber:
            if i >= currentlowestnumber and i-currentlowestnumber <= currentlowestnumber:
                print("Appending number to solution", i)
                solution.append(i)
                currentlowestnumber = i

    else:
        print("Adding minimum number of first half quarter list to solution.")
        currentlowestnumber = lowestsecondhalfrestlist
        solution.append(lowestsecondhalfrestlist)

    print("Numbers after the lowest number in first half of final list are", finalsecondhalflistminnumber)


    #final sanitisation (because i cant write code properly)
    lowsolutionnumber = 0

    #needs to be terminated eventually after multiple passes
    #program needs to have error checking when splitting up the lists doesn't work properly
    while lowsolutionnumber < 5:
        for index, i in enumerate(solution):
            if index == 0:
                continue

            print("Current number is ", i)
            print("Previous number is ", solution[index-1])

            if i < solution[index-1]:
                print(i, "is less than", solution[index-1])
                print("Removing: ", solution[index])
                del solution[index]

        lowsolutionnumber = lowsolutionnumber + 1


print("Peaks traversed are: ", solution)



#process, going from lowest peak to next peak, with smallest increments, making sure as many peaks as possible,
#and not going back to that peak 
# 10 and above - work by examining shortest from quarters, provided that shortest number in list is present in quarter 

#algorithm - first quarter of list used to find lowest number to build up from
# next quarters scanned for the lowest increasing increment up until the end

# list of 1 2 3 4
# scan through 1, find 1 as the lowest
# scan through 2, find 2 as the lowest, and higher than 1
# scan through 3, find 3 as the lowest, and higher than 2
# scan through 4, find 4 as the lowest, and higher than 3