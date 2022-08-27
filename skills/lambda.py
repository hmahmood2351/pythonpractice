add10 = lambda x:x+10

print(add10(10))

mult = lambda x,y:x*y
print(mult(2,7))


testlist = [(11,5),(3,4),(5,6)]
sortedtestlist = sorted(testlist, key=lambda x:x[0] + x[1])
print(testlist)
print(sortedtestlist)


testlist2 = [1,2,3,4,6]
testlist3 = [1,2,3]
print(testlist2)
testlist2mapped = map(lambda x:x+1, testlist2)
print(list(testlist2mapped))

x = [i+2 for i in testlist2]
print(x)

testlist3mapped = filter(lambda x:x>=2, testlist3)
print(list(testlist3mapped))

from functools import reduce

testlist4 = [1,2,3,4]
testlist4mapped = reduce(lambda x,y:x*y, testlist4)
print(testlist4mapped)
