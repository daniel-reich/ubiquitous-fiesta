
def pie_chart(data):
  fract  = 360/sum(data.values())
  return {key: round(value * fract, 1) for key, value in data.items()}

