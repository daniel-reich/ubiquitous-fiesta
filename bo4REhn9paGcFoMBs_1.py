
def age_difference(ages):
    z, y, *_ = sorted(ages, reverse=True)
    return {
        0: "No age difference between spouses.",
        1: "1 year",
    }.get(z - y, "{} years".format(z - y))

