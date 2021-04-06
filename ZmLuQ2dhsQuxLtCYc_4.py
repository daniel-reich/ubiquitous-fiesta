
import datetime as dt
def energy_bill(s_date, e_date, s_read, e_read, tariff, stand):
  s=dt.datetime.strptime(s_date, "%Y,%m,%d")
  e=dt.datetime.strptime(e_date, "%Y,%m,%d")
  td=(e-s).days
  Tu=(e_read-s_read)*tariff
  Ts=td*stand
  ans=round(Tu+Ts+(Tu+Ts)*0.05,2)
  if td<0:
    return "Invalid date"
  if Tu<0:
    return "Invalid meter readings"
  return '${}'.format(ans)

