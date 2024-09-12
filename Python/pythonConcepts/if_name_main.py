""" 1 .default value of __name__ is '__main__' (you can verify it in python editor),
2. This is a predefined variable in python which gets set as '__main__'
3. It is used as an entry point for any python program.
4. Like in C : "void main()"
5. if we call this function from other file like 'caller.py' the value of __name__ is the module name i.e if_name_main
  run the caller.py and you will know the difference.
"""

def calculate_area(base,height):
    print("__name__ : ", __name__)
    return 1/2*(base*height)

if __name__ == "__main__":
    print("I am in if_name_main.py")
    a = calculate_area(10,20)
    print("area : ", a)