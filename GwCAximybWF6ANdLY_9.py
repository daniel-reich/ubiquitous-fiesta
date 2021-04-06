
def pie_chart(data):
  total = 0
  for item in data:
    total+=data[item]
  for item in data:
    data[item]=round(data[item]*360/total, 1)
  return data

