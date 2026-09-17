# Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java


with open("07_file_input_output_in_python/practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning file I/O")
    f.write("\nusing Java.")
    f.write("I like programming in Java.")
