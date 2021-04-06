
def BMR(person):
    age, gender, size, sport, weight = [v for k, v in sorted(person.items())]
    if gender == 'male':
        bmr = 66.47 + 13.75*weight + 5.003*size - 6.755*age
    else:
        bmr = 655.1 + 9.563*weight + 1.85*size - 4.676*age
    return round(bmr * [1.2, 1.375, 1.55, 1.725, 1.9][sport-1], 1)

