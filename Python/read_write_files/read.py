with open("C:\\shweta\\Courses\\Python\\read_write_files\\funny.txt","r") as f:     # When file is Opened with "With" statement then it will automatically close this file at the run end
    f_out = open("C:\\shweta\\Courses\\Python\\read_write_files\\funny_copy.txt","w")
    #print(f.read())
    for line in f:
        tokens = line.split(' ') # it will return the list of words in each line
        f_out.write(line + " Wordcount: " + str(len(tokens)))
        f_out.write("\n")
        print(str(tokens))
        print(len(tokens))
    f_out.close()
