# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

# def count_evens(nums):
#   return len([i for i in nums if i % 2 == 0])

# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8

# def big_diff(nums):
#   return max(nums) - min(nums)

# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

# testlist1 = [1,2,3,4,5]
# testlist2 = [1,2,3,4,5,6]

# print(testlist1)
# print(testlist2)

# print( (len(testlist1)//2) )
# print( testlist1[len(testlist1)//2], "is the middle" )
# print( testlist1[(len(testlist1)//2):] )
# print( testlist1[:(len(testlist1)//2)] )

# if len(testlist1[(len(testlist1)//2):]) < len(testlist1[:(len(testlist1)//2)]):
#     print("First shorter than second")
#     print("Average is: ")
#     print(testlist1[len(testlist1)//2] + testlist1[len(testlist1)//2+1] / 2)
# elif len(testlist1[:(len(testlist1)//2)]) < len(testlist1[(len(testlist1)//2):]):
#     print("Second shorter than first")
#     print("Average is: ", testlist1[len(testlist1)//2], testlist1[len(testlist1)//2+1])
#     print(testlist1[len(testlist1)//2] + testlist1[len(testlist1)//2+1] / 2)
# else:
#     print("Equal length.")


# print( (len(testlist2)//2) )

# def centered_average(nums):
#   nums.remove(min(nums))
#   nums.remove(max(nums))
#   mylist = []
#   total = 0
#   for i in nums:
#     if nums.count(i) > 1 and i not in mylist:
#       mylist.append(i)
#       nums.remove(i)
#   for i in nums:
#     total += i 
#   average = total/len(nums)
#   return average

# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

# def sum13(nums):
#   newlist = []
#   if len(nums) == 0:
#     return 0
#   for index, i in enumerate(nums):
#     if i == 13:
#       nums = nums[:index]
#       break
#     if i == 13 and index == 0:
#       newlist.append(0)
#     newlist.append(i)
#   return sum(newlist)

# wrong tests defined? seems to be working

# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

# def sum67(nums):
#   sixspotted = False
#   sixspottedindex = 0
#   sevenspotted = False
#   sevenspottedindex = 0
#   for index, i in enumerate(nums):
#     if i == 6 and sixspotted == False:
#       sixspotted = True
#       sixspottedindex = index
#     if i == 7 and sevenspotted == False and sixspotted == True:
#       sevenspotted = True
#       sevenspottedindex = index
#     if sixspotted == True and sevenspotted == True and sixspottedindex < sevenspottedindex:
#       for jindex, j in enumerate(nums):
#         if jindex >= sixspottedindex and jindex <= sevenspottedindex:
#           nums[jindex] = 0
#       sixspotted = False
#       sevenspotted = False
#       sixspottedindex = 0
#       sevenspottedindex = 0
#   return sum(nums)

# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

# def has22(nums):
#   if len(nums) >= 2:
#     for index, i in enumerate(nums):
#       if index == 0 and i == 2:
#         if nums[1] == 2:
#           return True 
#       if index == len(nums)-1 and i == 2:
#         if nums[len(nums)-2] == 2:
#           return True
#       if index != 0 and index != len(nums)-1 and i == 2:
#         if nums[index-1] == 2 or nums[index+1] == 2:
#             return True
#   return False