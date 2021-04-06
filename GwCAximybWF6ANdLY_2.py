
def pie_chart(data):
  total = sum(v for k,v in data.items())
  for key in data:
    data[key] *= 360/total
    data[key] = round(data[key],1)
  return data

