from itertools import *
from tokenize import group 

testlist = [1,2,3,4]
testlist2 = [11,9,7]
prod = product(testlist, testlist2)

permutationlist = permutations(testlist, 2)

combinationlist = combinations(testlist, 2)

combinationlistreplace = combinations_with_replacement(testlist,2)

accumulatelist = accumulate(testlist)

#alt to lambda func 
def smallerthan3(x):
    return x < 3

groupbylist = groupby(testlist, key=lambda x:x<3)
for key, value in groupbylist:
    print(key, list(value))

for i in count(10):
    print(i)
    if i == 15:
        break

# for i in cycle(testlist):
#     print(i)
    
# for i in repeat(testlist):
#     print(i)

