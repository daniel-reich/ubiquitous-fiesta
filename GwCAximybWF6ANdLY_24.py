
def pie_chart(data):
  freq_total = sum(data.values())
  output = {}
  for p in data.keys():
    output[p] = float('{:0.1f}'.format(data[p] / freq_total * 360))
  return output

