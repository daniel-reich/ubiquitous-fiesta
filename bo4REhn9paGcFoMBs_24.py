
def age_difference(ages):
    ages.sort()
    diff = ages[-1] - ages[-2]
    return "No age difference between spouses." if not diff \
    else "{} year{}".format(diff, ["", "s"][diff > 1])

