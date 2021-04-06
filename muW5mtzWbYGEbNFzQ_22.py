
multipliers = {1 : 1.2, 2 : 1.375, 3 : 1.55, 4 : 1.725, 5 : 1.9}
def BMR(person):
    multiplier = multipliers[person["sport"]]
    if person["gender"] == "male":
        return round( (66.47 + (13.75 * person["weight"]) + (5.003 * person["height"]) - (6.755 * person["age"]) ) * multiplier, 1)
    else:
        return round( (655.1 + (9.563 * person["weight"]) + (1.85 * person["height"]) - (4.676 * person["age"]) ) * multiplier, 1 )

