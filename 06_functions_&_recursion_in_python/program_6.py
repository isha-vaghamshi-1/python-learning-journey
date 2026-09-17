# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

def print_list(list, index):
    if index == len(list):
        return
    else:
        print(list[index])
        print_list(list, index+1)

print_list([1, 2, 3, 4, 5], 0)