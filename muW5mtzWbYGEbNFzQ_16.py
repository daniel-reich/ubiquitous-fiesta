
exercise_factors = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
​
def BMR(person):
    if person["gender"] == "male":
        bmr = 66.47 + 13.75 * person["weight"] + 5.003 * person["size"] - 6.755 * person["age"]
    else:
        bmr = 655.1 + 9.563 * person["weight"] + 1.85 * person["size"] - 4.676 * person["age"]
    bmr *= exercise_factors[person["sport"]]
    return round(bmr, 1)

