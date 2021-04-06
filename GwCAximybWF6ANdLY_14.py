
def pie_chart(data):
  print(data)
  total = (sum(data.values()))
  for k, v in data.items():
    data[k] = round((v / total) * 360, 1 )
  return data

