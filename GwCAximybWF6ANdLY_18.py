
def pie_chart(data):
  return {k:round(v*(360/sum(data.values())), 1) for k,v in data.items()}

