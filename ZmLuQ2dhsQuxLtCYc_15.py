
from datetime import date
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
  start_date=[int(i) for i in start_date.split(',')]
  end_date=[int(i) for i in end_date.split(',')]
  dbetween=int((date(end_date[0],end_date[1],end_date[2])-date(start_date[0],start_date[1],start_date[2])).days)
  if dbetween<0:return 'Invalid date'
  dmeter=end_read-start_read
  if dmeter<0:return 'Invalid meter readings'
  return '$'+str(round(((dbetween*stand) + (dmeter*tariff))*1.05 ,2))

