
def describe_num(n):
  d = {1:'brilliant', 2:'exciting', 3:'fantastic', 4:'virtuous', 5:'heart-warming', 6:'tear-jerking', 
       7:'beautiful', 8:'exhillarating', 9:'emotional', 10:'inspiring'}
  return 'The most '+' '.join([ d[i] for i in range(1,11) if n % i == 0])+" number is " + str(n) +'!'

