
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
even = 0
number = 0
while True:
    num = int(input())
    if number > 10:
        break
    elif num % 2 == 0:
        even += 1
        number += 1
        continue
    else:
        even = 0
        number += 1
        continue
print(even)