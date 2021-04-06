
def get_day(day):
    from datetime import datetime
    return datetime.strptime(day, '%m/%d/%Y').strftime('%A')

