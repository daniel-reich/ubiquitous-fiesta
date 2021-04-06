
def leap_year(yr):
    return ((not yr%4) + (not yr%100) + (not yr%400))%2

