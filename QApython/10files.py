#tutorial

# file = open('QApython/filename.txt', 'r')

# outfile = ""

# for line in range(1,10):
#     if line % 2 == 0:
#         outfile = outfile + file.readline()
#     else:
#         file.readline()

# file = open("QApython/filename.txt", "w")
# file.write(outfile)
# file.close()


#exercise

file = open("teams.txt", "w")
team = ['wolf', 'bears', 'ravens']

for i in team:
    file.write(i + '\n')
file.close()


read_file = open('teams.txt', 'r')

lines = read_file.readlines()
print(lines[0])

read_file.close()