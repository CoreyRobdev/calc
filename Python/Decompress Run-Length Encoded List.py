from collections import Counter

nums = [1,2]

for x in range(len(nums)):
  if x%2==0:
    b = x
  else:
    a = x
c = Counter(b=a)
print(c)