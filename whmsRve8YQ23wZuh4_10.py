
import re
​
​
def sort_dates(lst, mode):
    reverse =  True if mode == 'DSC' else False
    dates = [re.split('_|-|:', i) for i in lst]
    dates.sort(key=lambda x: x[4], reverse=reverse)
    dates.sort(key=lambda x: x[3], reverse=reverse)
    dates.sort(key=lambda x: x[0], reverse=reverse)
    dates.sort(key=lambda x: x[1], reverse=reverse)
    dates.sort(key=lambda x: x[2], reverse=reverse)
    return ['{}-{}-{}_{}:{}'.format(*date) for date in dates]

