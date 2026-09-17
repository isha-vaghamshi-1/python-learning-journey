# Search if the word “learning” exists in the file or not.

Word = 'learning'

with open('07_file_input_output_in_python/practice.txt', 'r') as file:
    for line in file:
        print(line)
        if Word in line:
            print(f"The word '{Word}' exists in the file.")
            break
        else:
            print(f"The word '{Word}' does not exist in the file.")
            