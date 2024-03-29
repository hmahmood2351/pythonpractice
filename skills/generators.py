import sys 

def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

print(sorted(g))


def firstn(n):
    nums = []
    num = 0

    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))