
def pie_chart(data):
  total = sum(data.values())
  for i in data.keys():
    data[i] = round(data[i]/total * 360,1)
  return(data)

