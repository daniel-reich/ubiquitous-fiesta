
def BMR(person):
    (gender, size, weight, age, sport) = (person['gender'], person['size'], person['weight'], person['age'], person['sport'])
    sport = [1.2, 1.375, 1.55, 1.725, 1.9][sport - 1]
    if gender == 'male':
        return round((66.47 + (13.75 * weight) + (5.003 * size) - (6.755 * age))*sport, 1)
    if gender == 'female':
        return round((655.1 + (9.563 * weight) + (1.85 * size) - (4.676 * age))*sport, 1)

