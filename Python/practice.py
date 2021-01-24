# 1342. Number of Steps to Reduce a Number to Zero
x = int(input("Input: num = "))
steps = 0
while x != 0:
    steps += 1

    if x % 2 == 0:
        x /= 2
    else:
        x -= 1
print("Output: " + str(steps))
