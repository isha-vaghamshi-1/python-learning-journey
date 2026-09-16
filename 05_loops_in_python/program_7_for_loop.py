# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]


numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x = 36
idx = 0

for item in numbers:
    if(item==x):
        print("we found the number", x, "at", idx)       
        break
    idx += 1