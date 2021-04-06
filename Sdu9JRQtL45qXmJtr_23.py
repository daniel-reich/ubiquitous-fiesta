
import string
​
def happy_birthday(age):
    base_twenty = 0
    base_twenty_one = 0
    incrementer = 3
    ### test 20
    while base_twenty < age:
        base_twenty = int_to_base(20,incrementer)
        incrementer += 1
    if base_twenty == age:
        return 'Mubashir is just 20, in base {}!'.format(incrementer-1)
    incrementer = 3
    while base_twenty_one < age:
        base_twenty_one = int_to_base(21,incrementer)
        incrementer += 1
    if base_twenty_one == age:
        return 'Mubashir is just 21, in base {}!'.format(incrementer-1)
        
def int_to_base(num,base):
    total = 0
    str_number = str(num)
    power_increment = 1
    for eachletter in str_number:
        total += int(eachletter) * base**power_increment
        power_increment -= 1
    return total

