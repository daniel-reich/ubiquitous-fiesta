
def pie_chart(data):
  su = sum(data.values())
  for key,value in data.items():
    data[key] = float(format((value/su)*360,'0.1f'))
  return data

