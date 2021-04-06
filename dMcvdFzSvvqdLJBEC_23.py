
def num_of_days(cost, savings, start):
    needed = cost - savings
    week= 0
    day = 0
    week = 0
    summe = 0
    while True:
        monday= start + week
        week += 1
        for day in range(7):
            summe += monday + day
            if summe >= needed:
               return week*7 - (6-day)

