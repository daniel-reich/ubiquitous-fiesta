
def time_sum(times):
  segundos=0
  for x in times:
    x=x.split(":")
    segundos=segundos+(int(x[0])*3600)
    segundos=segundos+(int(x[1])*60)
    segundos=segundos+(int(x[2]))
  hora=segundos//3600
  minuto=(segundos%3600)//60
  segundo=(segundos%3600)%60
  return [hora,minuto,segundo]

