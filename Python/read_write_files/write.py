f = open("C:\\shweta\\Courses\\Python\\read_write_files\\funny.txt","w")
f.write("I love Javascript")  # Write mode will overwrite the existing contents
f.close()  # Closing a file will free up all the resources os allocated for this file

f = open("C:\\shweta\\Courses\\Python\\read_write_files\\funny.txt","a")
f.write("\nI love python")  # Append mode will append the text to the existing contents
f.close()
