try:
    f = open("C:\\shweta\\Courses\\Python\\read_write_files\\funnyq.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError as e:
    print(e)

