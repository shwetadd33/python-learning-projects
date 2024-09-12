
exp = [324,5453,6436,4353,2322,2322]
total = 0
for i in range(len(exp)):
    print('Month: ', (i+1), 'Expense:', exp[i])
    total = total+exp[i]
    print("My total expense is: ", total)