import copy 

org = [1,2,3]
cpy = copy.deepcopy(org)
org[0] = -10
print(org)
print(cpy)
