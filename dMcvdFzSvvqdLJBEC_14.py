
def num_of_days(cost, savings, start):
    days = 0
    while savings < cost:
        temp = start
        for i in range(7):
            if cost > savings:
                savings = savings +temp
                temp =temp+1
                days= days+1
        start = start+1
    return(days)

