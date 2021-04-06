
def pie_chart(data):
  return {d:round(float(data[d])/sum(data.values())*360,1) for d in data}

