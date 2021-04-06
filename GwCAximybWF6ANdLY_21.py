
def pie_chart(data):
  summ=0
  for k, v in data.items():
    summ+=v
  return {k:(int(v/summ*360) if int(v/summ*360)==v/summ*360
          else round(v/summ*360,1)) for k,v in data.items()}

