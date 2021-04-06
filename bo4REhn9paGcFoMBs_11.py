
def age_difference(ages):
    oldest = max(ages)
    ages.remove(oldest)
    a = oldest - max(ages)
    if a == 0:
        return "No age difference between spouses."
    elif a == 1:
        return "1 year"
    else:
        return "{} years".format(a)

