
def age_difference(ages):
    ages = sorted(ages)
    a = ages[-1] - ages[-2]
    if a == 1:
        return str(a) + ' year'
    if a > 1:
        return str(a) + ' years'
    elif a == 0:
        return 'No age difference between spouses.'

