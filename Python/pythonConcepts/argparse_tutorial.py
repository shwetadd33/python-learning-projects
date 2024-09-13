"""
command line arguments -

1. Positional args : all the arguments must be passed through command line i.e. all the args are mandatory
2. Operational args: if want to skip some args , use optional args . just use -- before the arguments
"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num1",help="1st number")
    parser.add_argument("num2",help="2nd number")
    parser.add_argument("--num3",help="3rd number")
    parser.add_argument("operation",help="Operation to perform", choices=["add","subtract","multiply"])
    args = parser.parse_args()

    print(args.num1)
    print(args.num2)
    print(args.num3)
    print(args.operation)

    n1 = int(args.num1)
    n2 = int(args.num2)
    result = None

    if args.operation == "add":
        result = n1+n2
    elif args.operation == "subtract":
        result = n1-n2
    elif args.operation == "multiply":
        result = n1*n2

    print("Result:",result)
