# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

Classroom={}

math = input("Enter the marks of the math: ")
science = input("Enter the marks of the science: ")
history = input("Enter the marks of the history: ")

Classroom["math"] = math
Classroom["science"] = science
Classroom["history"] = history

print(Classroom)