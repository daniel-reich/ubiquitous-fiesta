
def leap_year(yr):
    return ((yr%4==0) +(str(yr)[2:]=='00')-(yr%400==0))==1

