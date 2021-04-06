
import datetime
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
​
  start_year = int(start_date.split(',')[0])
  start_month = int(start_date.split(',')[1])
  start_day = int(start_date.split(',')[2])
  
  end_year = int(end_date.split(',')[0])
  end_month = int(end_date.split(',')[1])
  end_day = int(end_date.split(',')[2])
  
  date1 = datetime.date(start_year,start_month,start_day)
  date2 = datetime.date(end_year,end_month,end_day)
  
  amount_of_days_between_two = (date2 - date1).days
  if amount_of_days_between_two < 0:
    return 'Invalid date'
  
  total_misc = (amount_of_days_between_two * stand) + ((end_read - start_read)*tariff)
  the_total_cost = total_misc + (total_misc * 0.05)
  
  return '${}'.format(round(the_total_cost,2)) if the_total_cost > 0 else 'Invalid meter readings'

