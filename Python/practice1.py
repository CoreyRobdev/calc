# 1108. Defanging an IP Address
def defang(IP):
    defang = ""
    for letter in IP:
        if letter in ".":
            defang = defang + "[.]"
        else:
            defang = defang + letter
    return defang


print(defang(input("Enter IP: ")))
