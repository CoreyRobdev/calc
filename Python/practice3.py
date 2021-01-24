input = input("nums: ")
a = []
o = []
for x in input:
    a.append(x)


for x in range(len(a)):
    q = x + 2
    if x % 2 != 0:
        for z in range(int(a[-2])):
            o.append(a[-1])
print(o)
