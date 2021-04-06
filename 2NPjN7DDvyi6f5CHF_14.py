
def age_difference(f_age, s_age):
    diff = f_age - s_age
    s = 1
    f = 1 + diff
    while s < f:
        if f == s*2:
            if f < f_age:
                return f_age - f
                break
            elif f > f_age:
                return f - f_age
                break
            else:
                return 0 
                break
        else:
            s += 1
            f += 1
            continue

