
def weekly_salary(lst):
    result = 0
    for l in lst[:5]:
        if 0 < l <= 8:
            result = result + l*10
        elif l > 8:
            result = result + 8*10 + (l-8)*15
    for l in lst[5:]:
        if 0 < l <= 8:
            result = result + l * 20
        elif l > 8 :
            result = result + 8*20 + (l - 8) * 30
    return result

