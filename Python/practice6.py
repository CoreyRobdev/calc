'''
Given an array nums of integers, return how many of them contain an even number of digits.
Input: nums = [12,345,2,6,7896]
Output: 2
'''
e =0
nums = []
while e != -1:
  e = int(input("Enter number (-1 to exit): "))
  nums.append(e)

print(len(list(filter(lambda x: len(str(x+1))%2==0, nums))))
