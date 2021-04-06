
def afterNdays(days, n):
  w = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
  return [w[(w.index(i)+n)%7] for i in days]

