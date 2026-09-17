# WAF to print the elements of a list in a single line. ( list is the parameter)

def print_list(list):
    for i in list:
        print(i, end='  ')

print_list([1, 2, 3, 4, 5])
