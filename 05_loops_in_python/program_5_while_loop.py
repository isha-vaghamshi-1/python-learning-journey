# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

list = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = 36
n = 0

while (n < len(list)):
    if(list[n] == x):
        print('Found the number', x, "at index", n)    
    n+=1
    
