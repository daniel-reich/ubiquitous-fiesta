
def BMR(person):
    men_bmr = lambda weight, size, age: 66.47 + (13.75 * weight) + (5.003 * size) - (6.755 *age)
    women_bmr = lambda weight, size, age: 655.1 + (9.563 * weight) + (1.85 * size) - (4.676 *age)
    if person["gender"] == "male":
        bmr =  men_bmr(person["weight"],person["size"], person["age"])
    else:
        bmr = women_bmr(person["weight"],person["size"], person["age"])
    switcher = {
        0:bmr * 1.2,
        1:bmr * 1.2,
        2:bmr * 1.375,
        3:bmr * 1.55,
        4:bmr * 1.725,
        5:bmr * 1.9
    }
    return round(switcher.get(person['sport'],bmr*1.9),1)

