
def calc_diff(obj, limit):
    return sum(obj.values()) - limit
print(calc_diff({'baseball bat': 20},5))
print(calc_diff({'skate': 10, 'painting': 20},19))
print(calc_diff({'skate': 200, 'painting': 200, 'shoes': 1},400))

