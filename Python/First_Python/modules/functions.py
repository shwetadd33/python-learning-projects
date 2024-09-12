def total_expense(items_list):

    total = 0
    for item in items_list:
        total = total+item
    return total

'''
tom_exp = [2144,3242,232,1224,2323]
joe_exp = [2321,435,6565,2322,1111]
toms_total = total_expense(tom_exp)
joes_total = total_expense(joe_exp)

print("Tom's expense : ", toms_total)
print("Joe's expense : ", joes_total)
'''