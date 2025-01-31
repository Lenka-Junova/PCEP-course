# 3.6.1.9 LAB task - remove repetitions in a list
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
status = False
new_list = my_list[:]

for number in new_list:
    #if two or more the same, keep only 1 number
    if new_list[number] in new_list:
        number == number+1
        del new_list[number]
    else:
        status = True
        break

print("The list with unique elements only:")
print(new_list)
