
def pie_chart(data):
  suma = sum(data.values())
  for x in data:
    data[x] = round(data[x] * 360 / suma, 1)
  return data

