
from datetime import datetime
def sort_dates(lst, mode=None):
    b = [datetime.strptime(i, "%d-%m-%Y_%H:%M") for i in lst]
    if mode == "ASC":
        return [j for i,j in sorted(zip(b,lst))]
    else:
        return [j for i,j in sorted(zip(b,lst), reverse=True)]

