# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# [1, 2, 3, 2, 1] [1, “abc”, “abc”, 1]


list1 = [1, 2, 3, 2, 1]
list2 = [1, "abc", "abc", 1]

if list1 == list1[::-1]:
    print("List is a palindrome")
else:
    print("List is not a palindrome")

if list2 == list2[::-1]:
    print("List is a palindrome")
else:
    print("List is not a palindrome")