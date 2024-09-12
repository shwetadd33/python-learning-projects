from typing import TextIO


class Accident(Exception):  # Accident class is derived from Exception class which is a built-in class
    def __init__(self, msg):
        self.msg = msg

    def print_exception(self):
        print("User defined exception: ", self.msg)


class PageNotFound(Accident, Exception):
    def __init__(self, msg, w):
        self.msg = msg
        self.warning = w

    def print_warning(self):
        print("Warning: ", self.warning)


class process_file(Exception):
    def __init__(self, fn):
        self.filename = fn

    def process_current(self):
        try:
            f1 = open(self.filename, "r")
            x=1/0
            print(f1.read())

        except FileNotFoundError as e:
            print("File Not Found")

        finally:
            print("Cleaning up file")
            f1.close()
            if f1.closed:
                print("File closed....")
"""
try:
    raise Accident('Carsh')
except Accident as e:
    e.print_exception()

try:
    raise PageNotFound('Source not found', 'Try again')
except PageNotFound as p:
    p.print_exception()
    p.print_warning()
"""

pf = process_file("C:\\shweta\\Courses\\Python\\read_write_files\\funny1.txt")
pf.process_current()

