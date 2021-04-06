
def leap_year(yr):
    return (yr % 4 == 0)-(int(str(yr)[-1:-3:-1])==0)*((yr//100 % 4)>0)

