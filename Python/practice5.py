# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

a =[]
prod = 1
add = 0
n = str(input("Enter: "))
for x in n:
  a.append(x)
for x in range(len(a)):
  prod = int(a[x])*prod
for x in range(len(a)):
  add = add+int(a[x])
print("Output: " + str(prod - add))