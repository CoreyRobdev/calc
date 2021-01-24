"""
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:
  Characters ('a' to 'i') are represented by ('1' to '9') respectively.
  Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Input: s = "10#11#12"
Output: "jkab"
Input: s = "1326#"
Output: "acz"
"""

a1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'z', 'y', 'z']
a3 = []

s = input("Input: ")
# Creates input array
for intInString in s:
    if intInString != "#":
        a3.append(intInString)
    else:
        a3[-2] = a3[-2] + a3[-1]
        a3.pop()

# Translates numbers into letters
for charInArray in a3:
    charInArray = int(charInArray) - 1
    print(a1[int(charInArray)], end='')
