
from calendar import isleap
def num_of_leapyears(years):
    return sum([isleap(x) for x in range(int(years.split('-')[0]), int(years.split('-')[1])+1)])

