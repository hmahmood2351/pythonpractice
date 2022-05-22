author = ['nietzsche']
quote = 'He who has a why to live for can bear almost any how'

print(f"{author[0]} once said, '{quote}'")

x = author.pop()

author.insert(0,'A')
author.insert(1,'B')
print(author)


y = [x**2 for x in range(1,11)]
print(y)

twenny = [x for x in range(1,21)]
print('twenny', twenny)

milly = [x for x in range(1,1_000_001)]
print('min', min(milly))
print('max', max(milly))

oddtwenny = [x for x in range(1,21) if x%2!=0]
print('oddtwenny', oddtwenny)

threes = [x for x in range(1,31) if x%3==0]
print('threes', threes)

cubes = [x**3 for x in range(1,11)]
print('cubes', cubes)

my_foods=['pie']
friend_foods=my_foods[:]
print(my_foods)
friend_foods.append('test')
print(my_foods, friend_foods)

tuple1 = (1,2)
print(tuple1)
tuple1 = (2,3)
print(tuple1)

if my_foods:
    print("Not empty")