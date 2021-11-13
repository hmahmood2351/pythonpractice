# Our maze explorer has some weird rules for finding the exit. 
# It is up to you find out if it is possible with the following rules, whether they will escape.
# Our explorer has the following rules:
# They always walk 6 blocks straight and then turn 180° and start walking 6 blocks again.
# If a wall is in their way they turn to the right, if that not possible they turn to the left and 
# if that is not possible, they turn back from where they came.

# Legend:
# >: Explorer looking East
# <: Explorer looking West
# ^: Explorer looking North
# v: Explorer looking south
# E: Exit
# #: wall
#  : Clear passage way (empty space)

# Enter a maze:
# ####### 
# #>   E#	
# #######

# Escaped!


# Enter a maze:
# #####E#
# #>    #	
# #######
# Escaped!


# ##########
# #>      E#
# ##########
# Trapped!

#functions 

#parsing maze - changing whitespace into _

def parsemaze(maze):
    newmaze = []
    for i in maze:
        if ' ' not in i:
            newmaze.append(i)
            continue
        else:
            newi = i.replace(' ', '_')
            newmaze.append(newi)
    return newmaze


#finding which line and position the player is on
def checkline(maze):
    linepos = {}
    for index, i in enumerate(maze):
        for jindex, j in enumerate(i):
            if j in acceptedcharacters[:4]:
                linepos = {'line':index,'pos':jindex}
                return linepos

#finding what direction the player is in 

def finddirection(maze):
    coords = checkline(maze)
    player = maze[coords['line']][coords['pos']]
    direction = ''
    
    if player == '>':
        direction = 'EAST'
        return direction 
    elif player == '<':
        direction = 'WEST'
        return direction
    elif player == '^':
        direction = 'NORTH'
        return direction
    elif player == 'v':
        direction = 'SOUTH'    
        return direction

#checking what's directly in front of the player six spaces forward (depending on direction)

def findinginfront(maze):
    coords = checkline(maze)
    direction = finddirection(maze)
    vision = ''

    if direction == 'EAST':

        vision = maze[coords['line']]
        return vision

    elif direction == 'WEST':

        vision = maze[coords['line']]
        return vision

    elif direction == 'SOUTH':

        for index, i in enumerate(maze): 
            for jindex, j in enumerate(i):
                if jindex == coords['pos']:
                    vision = vision + j
        return vision

    elif direction == 'NORTH':

        for index, i in enumerate(maze): 
            for jindex, j in enumerate(i):
                if jindex == coords['pos']:
                    vision = vision + j
        return vision

#finding block directly in front 

def dealingdirectlyinfront(maze):
    coords = checkline(maze)
    direction = finddirection(maze)
    vision = findinginfront(maze)
    found = ''

    if direction == 'EAST':
        coords['pos'] = coords['pos'] + 1 
        if maze[coords['line']][coords['pos']] == '#':
            found = 'WALL'
            return found 
        elif maze[coords['line']][coords['pos']] == 'E':
            found = 'EXIT'
            return found
        elif maze[coords['line']][coords['pos']] == '_':
            found = 'EMPTY'
            return found

    elif direction == 'WEST':
        coords['pos'] = coords['pos'] - 1
        if maze[coords['line']][coords['pos']] == '#':
            found = 'WALL'
            return found 
        elif maze[coords['line']][coords['pos']] == 'E':
            found = 'EXIT'
            return found
        elif maze[coords['line']][coords['pos']] == '_':
            found = 'EMPTY'
            return found

    elif direction == 'NORTH':
        coords['line'] = coords['line'] - 1 
        if maze[coords['line']][coords['pos']] == '#':
            found = 'WALL'
            return found 
        elif maze[coords['line']][coords['pos']] == 'E':
            found = 'EXIT'
            return found
        elif maze[coords['line']][coords['pos']] == '_':
            found = 'EMPTY'
            return found

    elif direction == 'SOUTH':
        coords['line'] = coords['line'] + 1
        if maze[coords['line']][coords['pos']] == '#':
            found = 'WALL'
            return found 
        elif maze[coords['line']][coords['pos']] == 'E':
            found = 'EXIT'
            return found
        elif maze[coords['line']][coords['pos']] == '_':
            found = 'EMPTY'
            return found

#moving 1 spaces forward (in respective direction)

def moveforwardone(maze):
    coords = checkline(maze)
    direction = finddirection(maze)
    vision = findinginfront(maze)
    infront = dealingdirectlyinfront(maze)
    newmaze = []
    newmaze2 = []

    if direction == 'EAST':

        #oldpos remove
        for i in maze:
            if '>' in i:
                newi = i.replace(">","_")
                newmaze.append(newi)
            else:
                newmaze.append(i)

        #newpos set    
        coords['pos'] = coords['pos'] + 1 
        for index, i in enumerate(newmaze):
            if index != coords['line']:
                newmaze2.append(i)
            for jindex, j in enumerate(i):
                if index == coords['line'] and jindex == coords['pos']:
                    newi = list(i)
                    newi[coords['pos']] = '>'
                    newi = "".join(newi)
                    newmaze2.append(str(newi))

        return newmaze2
        
    elif direction == 'WEST':
        
         #oldpos remove
        for i in maze:
            if '<' in i:
                newi = i.replace("<","_")
                newmaze.append(newi)
            else:
                newmaze.append(i)

        #newpos set    
        coords['pos'] = coords['pos'] - 1 
        for index, i in enumerate(newmaze):
            if index != coords['line']:
                newmaze2.append(i)
            for jindex, j in enumerate(i):
                if index == coords['line'] and jindex == coords['pos']:
                    newi = list(i)
                    newi[coords['pos']] = '<'
                    newi = "".join(newi)
                    newmaze2.append(str(newi))

        return newmaze2

    elif direction == 'NORTH':
        
        #oldpos remove
        for i in maze:
            if '^' in i:
                newi = i.replace("^","_")
                newmaze.append(newi)
            else:
                newmaze.append(i)

        #newpos set    
        coords['line'] = coords['line'] - 1 
        for index, i in enumerate(newmaze):
            if index != coords['pos']:
                newmaze2.append(i)
            for jindex, j in enumerate(i):
                if index == coords['line'] and jindex == coords['pos']:
                    newi = list(i)
                    newi[coords['pos']] = '^'
                    newi = "".join(newi)
                    newmaze2.append(str(newi))

        return newmaze2
    
    elif direction == 'SOUTH':
        #oldpos remove
        for i in maze:
            if 'v' in i:
                newi = i.replace("v","_")
                newmaze.append(newi)
            else:
                newmaze.append(i)

        #newpos set    
        coords['line'] = coords['line'] + 1 
        for index, i in enumerate(newmaze):
            if index != coords['pos']:
                newmaze2.append(i)
            for jindex, j in enumerate(i):
                if index == coords['line'] and jindex == coords['pos']:
                    newi = list(i)
                    newi[coords['pos']] = 'v'
                    newi = "".join(newi)
                    newmaze2.append(str(newi))

        return newmaze2

#changing player direction 180 degrees

def changedirection(maze):
    coords = checkline(maze)
    direction = finddirection(maze)
    vision = findinginfront(maze)
    newmaze = []

    if direction == 'EAST':
        for i in maze:
            if '>' not in i:
                newmaze.append(i)
            for j in i:
                if j == '>':
                    newi = list(i)
                    newi[coords['pos']] = '<'
                    newi = "".join(newi)
                    newmaze.append(str(newi))
        
        return newmaze
                    
    elif direction == 'WEST':
        for i in maze:
            if '<' not in i:
                newmaze.append(i)
            for j in i:
                if j == '<':
                    newi = list(i)
                    newi[coords['pos']] = '>'
                    newi = "".join(newi)
                    newmaze.append(str(newi))
        
        return newmaze

    elif direction == 'SOUTH':
        for i in maze:
            if 'v' not in i:
                newmaze.append(i)
            for j in i:
                if j == 'v':
                    newi = list(i)
                    newi[coords['pos']] = '^'
                    newi = "".join(newi)
                    newmaze.append(str(newi))
        
        return newmaze

    elif direction == 'NORTH':
        for i in maze:
            if '^' not in i:
                newmaze.append(i)
            for j in i:
                if j == '^':
                    newi = list(i)
                    newi[coords['pos']] = 'v'
                    newi = "".join(newi)
                    newmaze.append(str(newi))
        
        return newmaze

#changing direction (to its) right 
#east right is south
#west right is north
#south right is west
#north right is east

def changeright(maze):
    coords = checkline(maze)
    direction = finddirection(maze)
    vision = findinginfront(maze)
    newmaze = []

    if direction == 'EAST':
        for i in maze:
            if '>' not in i:
                newmaze.append(i)
            for j in i:
                if j == '>':
                    newi = list(i)
                    newi[coords['pos']] = 'v'
                    newi = "".join(newi)
                    newmaze.append(str(newi))
        
        return newmaze
                    
    elif direction == 'WEST':
        for i in maze:
            if '<' not in i:
                newmaze.append(i)
            for j in i:
                if j == '<':
                    newi = list(i)
                    newi[coords['pos']] = '^'
                    newi = "".join(newi)
                    newmaze.append(str(newi))
        
        return newmaze

    elif direction == 'SOUTH':
        for i in maze:
            if 'v' not in i:
                newmaze.append(i)
            for j in i:
                if j == 'v':
                    newi = list(i)
                    newi[coords['pos']] = '<'
                    newi = "".join(newi)
                    newmaze.append(str(newi))
        
        return newmaze

    elif direction == 'NORTH':
        for i in maze:
            if '^' not in i:
                newmaze.append(i)
            for j in i:
                if j == '^':
                    newi = list(i)
                    newi[coords['pos']] = '>'
                    newi = "".join(newi)
                    newmaze.append(str(newi))
        
        return newmaze

#changing direction (to its) left 
#east left is north
#west left is south
#south left is east
#north left is west

def changeleft(maze):
    coords = checkline(maze)
    direction = finddirection(maze)
    vision = findinginfront(maze)
    newmaze = []

    if direction == 'EAST':
        for i in maze:
            if '>' not in i:
                newmaze.append(i)
            for j in i:
                if j == '>':
                    newi = list(i)
                    newi[coords['pos']] = '^'
                    newi = "".join(newi)
                    newmaze.append(str(newi))
        
        return newmaze
                    
    elif direction == 'WEST':
        for i in maze:
            if '<' not in i:
                newmaze.append(i)
            for j in i:
                if j == '<':
                    newi = list(i)
                    newi[coords['pos']] = 'v'
                    newi = "".join(newi)
                    newmaze.append(str(newi))
        
        return newmaze

    elif direction == 'SOUTH':
        for i in maze:
            if 'v' not in i:
                newmaze.append(i)
            for j in i:
                if j == 'v':
                    newi = list(i)
                    newi[coords['pos']] = '<'
                    newi = "".join(newi)
                    newmaze.append(str(newi))
        
        return newmaze

    elif direction == 'NORTH':
        for i in maze:
            if '^' not in i:
                newmaze.append(i)
            for j in i:
                if j == '^':
                    newi = list(i)
                    newi[coords['pos']] = '<'
                    newi = "".join(newi)
                    newmaze.append(str(newi))
        
        return newmaze

################################## main ##################################

userinput = []
acceptedcharacters = ['>', '<', '^', 'v', 'E', '#', ' ']
directionschar = {'EAST':'>', 'WEST':'<', 'SOUTH':'v', 'NORTH':'^'}
onechar = 0

#printing out legend to the user

print()
print("Maze legend:")
print(">: Explorer looking East")
print("<: Explorer looking West")
print("^: Explorer looking North")
print("v: Explorer looking south")
print("E: Exit")
print("#: wall")
print(" : Clear passage way (empty space)")
print()


#input maze

print()
print("Please type in your maze, line by line.")
print("An unequal line length results in the program being terminated.")
print("Not including a player results in the line being terminated.")
print("Using characters not within the accepted characters list terminates the program.")
print()

while True:

    currentinput = input("Enter in line: ")

    if currentinput == 'end':


        lengthfirst = len(userinput[0])
        
        #error checking line length
        for i in userinput:
            if len(i) != lengthfirst:
                print("Error, incorrect line length.")
                userinput = []
                
        
        #error checking invalid characters
        for i in userinput:
            for j in i:
                if j not in acceptedcharacters:
                    print("Unaccepted character, ", j)
                    userinput = []

        #checking if player is present
        for i in userinput:
            for j in i:
                if j in acceptedcharacters[:4]:
                    onechar = onechar + 1
        
        if onechar != 1:
            print("Exceeded number of players/not included player")
            userinput = []
             

        else:
            break

    userinput.append(currentinput)


#parsing input for maze input and converting spaces to underline

parsedmaze = parsemaze(userinput)

#presenting to user

print()
print("Presenting maze to user: ")
for i in parsedmaze:
    print(i)


#printing what line the player is on

print()
print("Checking what line the player is on (adhering to starting from 0 as an index): ")

currentline = checkline(parsedmaze)

print("The line is: ", currentline['line'])
print("The position is: ", currentline['pos'])

#finding what direction the player is in 

founddirection = finddirection(parsedmaze)

print()
print("Finding direction the player is facing towards: ", founddirection)

#finding blocks in the vision of the player

foundvision = findinginfront(parsedmaze)

print()
print("The player has the blocks in his line of vision: ")
print(foundvision)

#finding what's directly in front of player

directlyinfront = dealingdirectlyinfront(parsedmaze)

print()
print("Player has the block in front of him: ")
print(directlyinfront)


#moving one space forward - checking done beforehand if # or E, empty space only 

# newmaze = moveforwardone(parsedmaze)

# print()
# print("Player is moving forward one block.")
# print("New maze is: ")

# for i in newmaze:
#     print(i)


# #changing direction 180 degrees

# newmaze = changedirection(newmaze)

# print()
# print("Player changing direction.")
# print("New maze is: ")

# for i in newmaze:
#     print(i)


# #changing direction right

# newmaze = changeright(newmaze)

# print()
# print("Player changing direction right.")
# print("New maze is: ")

# for i in newmaze:
#     print(i)

# #changing direction left 

# newmaze = changeleft(newmaze)

# print()
# print("Player changing direction left.")
# print("New maze is: ")

# for i in newmaze:
#     print(i)


#attempting to moving forward six times, back, and turning direction if encountered wall
#aka attempting to finally solve the problem

turncounterright = 0
turncounterleft = 0
gobackcounter = 0
escaped = 0
movecounter = 0

while True:
    try:

        for i in range(100):
            
            if movecounter == 6:
                break

            directlyinfront = dealingdirectlyinfront(parsedmaze)
            print("Block directly in front is: ", directlyinfront)

            if directlyinfront == 'EXIT':
                print("Escaped!")
                escaped = escaped + 1
                break
            
            while True:
                if directlyinfront == 'WALL' and turncounterright != 1:
                    parsedmaze = changeright(parsedmaze)
                    print("Changing direction, right")

                    for i in parsedmaze:
                        print(i)

                    directlyinfront = dealingdirectlyinfront(parsedmaze)
                    print("Block directly in front is: ", directlyinfront)

                    turncounterright = turncounterright + 1
                    break
                    
                if directlyinfront == 'WALL' and turncounterleft != 1:
                    parsedmaze = changedirection(parsedmaze)

                    print("Changing direction, left")

                    for i in parsedmaze:
                        print(i)

                    directlyinfront = dealingdirectlyinfront(parsedmaze)
                    print("Block directly in front is: ", directlyinfront) 

                    turncounterleft = turncounterleft + 1
                    break

                if directlyinfront == 'WALL' and gobackcounter != 1:
                    parsedmaze = changeleft(parsedmaze)

                    print("Changing direction, going back")

                    for i in parsedmaze:
                        print(i)

                    directlyinfront = dealingdirectlyinfront(parsedmaze)
                    print("Block directly in front is: ", directlyinfront)

                    gobackcounter = gobackcounter + 1
                    movecounter = 0
                    break
                
                if directlyinfront == 'WALL':
                    print("Trapped!")

                break
                
            directlyinfront = dealingdirectlyinfront(parsedmaze)
            print("Block directly in front is: ", directlyinfront)
            
            if directlyinfront == 'EXIT':
                print("Escaped!")
                escaped = escaped + 1
                break

            if directlyinfront == 'WALL':
                continue

            parsedmaze = moveforwardone(parsedmaze)
            movecounter = movecounter + 1

            print()
            print("Player is moving forward one block.")
            print("New maze is: ")

            for i in parsedmaze:
                print(i)

            print()
            print("Player has the block in front of him: ")
            print(directlyinfront)

        if escaped == 1:
            break
        else:
            print("Trapped!")
            break

    except IndexError:
          print("Trapped")
          break

    break