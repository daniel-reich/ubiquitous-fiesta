
day_minutes = 24*60
factor = day_minutes/24
meals = [factor*7, factor*12, factor*19]
​
def time_to_eat(current_time):
    time, during = current_time.split(' ')
    h, m = time.split(':')
​
    minutes = int(h)*60 + int(m)
    if during == 'p.m.':
        minutes += (day_minutes/2)
​
    remaining_to_meals = [meal - minutes for meal in meals]
    remaining_to_meals = list(map(lambda x: x <= 0 and x+day_minutes or x, remaining_to_meals))
​
    next_meal = int(sorted(remaining_to_meals)[0])
    return [next_meal//60, next_meal%60]

