
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
even = []
number = int(0)
while True:
    num = int(input())
    number += 1
    if num % 2 == 0:
        even.append(1)
        if number == 10:
            break
        else: continue
    else:
        even.clear()
        if number == 10:
            break
        else: continue
print(len(even))