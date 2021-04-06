
def pie_chart(data):
  frequencies_total = sum(data.values())
  for k in data.keys():
    data[k] = round(data.get(k)/frequencies_total*360,1)
    
  return data

