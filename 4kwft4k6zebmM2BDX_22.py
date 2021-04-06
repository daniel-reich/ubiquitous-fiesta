
def chi_squared_test(data):
  tot=sum(sum(data[i]) for i in data)
  data=[data[i] for i in data]
  mem=[[round(sum(data[j])*sum(data[k][i]/tot for k in range(len(data))),2) for i in range(len(data[0]))] for j in range(len(data))]
  x=round(sum([(data[i][j]-mem[i][j])**2/mem[i][j] for i in range(len(data)) for j in range(len(data[i]))]),1)
  return [x,("Edabitin effectiveness = 99%" if x>=6.635 else 'Edabitin effectiveness = 95%' if x>3.841 else 'Edabitin is ininfluent')]

