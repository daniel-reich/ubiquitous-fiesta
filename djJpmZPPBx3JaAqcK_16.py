
def maya_number(num):
    d=['@','o','oo','ooo','oooo','-','o-','oo-','ooo-','oooo-','--','o--','oo--','ooo--','oooo--','---','o---','oo---','ooo---','oooo---']
    maya_number = [] if num!=0 else ['@']
    while num>0:
        dig = num%20
        maya_number += [d[dig]]
        num //= 20
    return maya_number[::-1]

