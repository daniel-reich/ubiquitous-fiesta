
import datetime
def how_unlucky(y):
    
    # Get the first week day of the year
    return len([i for i in [datetime.datetime(y, j, 13).strftime("%A") for j in range(1, 13, 1)] if i == 'Friday'])

