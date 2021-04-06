
def pie_chart(data):
  total = sum(data.values())
  return {i:round(data[i]/total * 360, 1) for i in data}

