# WAF that replace all occurrences of “java” with “python” in above file.


with open("07_file_input_output_in_python/practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java", "python")
print(new_data)

with open("07_file_input_output_in_python/practice.txt","w") as f:
    f.write(new_data)