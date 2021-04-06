
def pie_chart(data):
  sum=0
  for i in data.values():
    sum+=i
  for i in data.keys():
    data[i]=round(((data[i]/sum)*360),1)
  return data

