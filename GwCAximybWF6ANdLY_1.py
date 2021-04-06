
def pie_chart(data):
  return {p: round(360*v/sum(data.values()), 1) for p, v in data.items()}

