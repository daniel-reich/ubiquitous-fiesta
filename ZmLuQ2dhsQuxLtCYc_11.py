
import datetime
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand, tax=.05):
    days = (convert_date(end_date) - convert_date(start_date)).days
    if days < 0:
        return 'Invalid date'
        
    read = end_read - start_read
    if read < 0:
        return 'Invalid meter readings'
        
    return '${:.2f}'.format((read*tariff + days*stand) * (1 + tax))
        
def convert_date(date):
    return datetime.datetime.strptime(date, "%Y,%m,%d").date()

