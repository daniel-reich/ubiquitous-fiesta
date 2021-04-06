
def weekly_salary(hours):
    x = 0
    for i in range(0,5):
        if hours[i] > 8:
            x += 15 * ( hours[i] - 8 ) + 80
        else:
            x += 10 * hours[i]
    for j in range(5,7):
        if hours[j] > 8:
            x += 30 * ( hours[j] - 8 ) + 160
        else:
            x += 20 * hours[j]
    return x

