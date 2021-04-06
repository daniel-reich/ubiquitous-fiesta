
def leap_year(yr):
    a = [yr%4==0,yr%100==0,yr%400==0]
    b = [[1,0,0],[1,1,1]]
    return a in b

