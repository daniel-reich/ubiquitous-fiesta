
def describe_num(n):
  s=""
  d = {1:'brilliant',
      2:'exciting',
      3:'fantastic',
      4:'virtuous',
      5:'heart-warming',
      6:'tear-jerking',
      7:'beautiful',
      8:'exhilarating',
      9:'emotional',
      10:'inspiring'}
  for i in d.keys():
    if n%i == 0:
      s += d[i]+ " "
      print(s)    
  return "The most {}number is {}!".format(s,n)

