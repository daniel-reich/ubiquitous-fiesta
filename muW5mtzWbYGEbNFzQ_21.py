
def BMR(person):
    mult = {1: 1.2,2: 1.375,3: 1.55, 4:1.725, 5:1.9}
    if person['gender'] == 'male':
        ans = (66.47 + (13.75 * person['weight']) + (5.003 * person['height']) - (6.755 * person['age'])) * mult[person['sport']]
    else:
        ans = (655.1 + (9.563 * person['weight']) + (1.85 * person['height']) - (4.676 * person['age'])) * mult[person['sport']]
    return round(ans,1)

