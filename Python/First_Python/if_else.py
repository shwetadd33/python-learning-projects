'''
    num = input("Enter a number: ")
num = int(num)

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

'''

indian = ["Samosa", "Pav Bhaji", "Daal", "Naan"]
chinese = ["Fried rice", "Manchurian", "Noodles"]
italian = ["Pasta", "Pizza", "risotto"]

dish = input("Enter a dish name : ")

if dish in indian:
    print("It's an Indian cuisine")
elif dish in chinese:
    print("It's a chinese cuisine")
elif dish in italian:
    print("It's an Italian cuisine")
else:
    print("Not known")

