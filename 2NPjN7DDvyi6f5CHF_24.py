
def age_difference(f_age, s_age):
    i=0
    while 2*(s_age+i)!=(f_age+i) and 2*(s_age-i)!=(f_age-i):
        i+=1
    return i

