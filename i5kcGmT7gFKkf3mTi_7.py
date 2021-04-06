
import datetime
def data_type(value):
  d={type('fg'):'string',type(51):'integer',type(1.02):'float',type([1,2]):'list',type(True):'boolean',type(datetime.date(2018,1,1)):'date',type({'a':1}):'dictionary'}
  return d[type(value)]

