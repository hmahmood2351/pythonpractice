# # # We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

# # # make_bricks(3, 1, 8) → True
# # # make_bricks(3, 1, 9) → False
# # # make_bricks(3, 2, 10) → True

# # # def make_bricks(small, big, goal):
# # #   return (goal%5)<=small and goal-(big*5)<=small

# # Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

# # lone_sum(1, 2, 3) → 6
# # lone_sum(3, 2, 3) → 2
# # lone_sum(3, 3, 3) → 0

# # def lone_sum(a, b, c):
# #   numbers = [a,b,c]
# #   for index, i in enumerate(numbers):
# #     if numbers.count(i) >= 2:
# #       numbers = [value for value in numbers if value != i]
# #   return sum(numbers)

# # Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

# # lucky_sum(1, 2, 3) → 6
# # lucky_sum(1, 2, 13) → 3
# # lucky_sum(1, 13, 3) → 1

# # def lucky_sum(a, b, c):
# #   listnumbers = [a, b, c]
# #   if 13 in listnumbers:
# #     listnumbers = listnumbers[:listnumbers.index(13)]
# #     return sum(listnumbers)
# #   return sum(listnumbers)

# # Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

# # no_teen_sum(1, 2, 3) → 6
# # no_teen_sum(2, 13, 1) → 3
# # no_teen_sum(2, 1, 14) → 3

# # def no_teen_sum(a, b, c):
# #   newlist = [a, b, c]
# #   for index, i in enumerate(newlist):
# #     if i >= 13 and i <= 19:
# #       if i == 15 or i == 16:
# #         continue
# #       newlist[index] = 0
# #   return sum(newlist)
  
# # For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().

# # round_sum(16, 17, 18) → 60
# # round_sum(12, 13, 14) → 30
# # round_sum(6, 4, 4) → 10

# # def round_sum(a, b, c):
# #   return int(round(a, -1) + round(b, -1) + round(c, -1))

# # Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

# # close_far(1, 2, 10) → True
# # close_far(1, 2, 3) → False
# # close_far(4, 1, 3) → True

# # def close_far(a, b, c):
# #   return ((abs(a-b) <= 1) or (abs(a-c) <= 1)) and ((abs(a-b) >= 2) or (abs(a-c) >= 2))

# def close_far(a, b, c):
#   if abs(a-b) <= 1:
#     if abs(a-c) >= 2 and abs(b-c) >= 2:
#       return True
#   elif abs(a-c) <= 1:
#     if abs(a-b) >= 2 and abs(c- b) >= 2:
#       return True
#   return False

# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 1, 10) → -1
# make_chocolate(4, 1, 7) → 2

# def make_chocolate(small, big, goal):
#   smallbarsleft = small
#   if big*5 <= goal:
#     smallbarsleft = goal-(big*5)
#   else:
#     smallbarsleft = goal%5
#   if smallbarsleft <= small:
#     return smallbarsleft
#   return -1