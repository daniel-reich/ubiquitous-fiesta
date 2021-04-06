
def pie_chart(data):
  tot=sum(data.values())
  for k, v in data.items():
    data[k]=round(v*360/tot,1)
  return data

