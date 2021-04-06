
def pie_chart(data):    
  datasum=sum(data[i] for i in data)
  for i in data:
    data[i]= round((data[i]/datasum)*360,1)   
  return data

