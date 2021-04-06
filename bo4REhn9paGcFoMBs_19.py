
def age_difference(ages):
    ages = sorted(ages)
    total_difference = ages[-1]-ages[-2]
    if total_difference == 0:
        return "No age difference between spouses."
    if total_difference == 1:
        return "{} year".format(total_difference)
    else:
        return "{} years".format(total_difference)

