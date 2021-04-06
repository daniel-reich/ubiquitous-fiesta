
from datetime import datetime
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
  sd = datetime.strptime(start_date,'%Y,%m,%d')
  ed = datetime.strptime(end_date,'%Y,%m,%d')
  d = (ed-sd).days
  if d<0: return 'Invalid date'
  r = end_read-start_read
  if r<0: return 'Invalid meter readings'
  ret = (d*stand)+(r*tariff)
  ret+=ret*.05
  ret = '$'+str(round(ret,2))
  ret+='0'*(2-len(ret.split('.')[1]))
  return ret

