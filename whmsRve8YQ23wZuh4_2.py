
from datetime import datetime as dt
sort_dates=lambda l,m:sorted(l,key=lambda x:dt.strptime(x,'%d-%m-%Y_%H:%M'),reverse=m=='DSC')

