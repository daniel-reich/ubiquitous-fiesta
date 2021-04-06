
def pie_chart(data):
  return {key: round((value/sum(data.values()))*360, 1) for key, value in data.items()}

