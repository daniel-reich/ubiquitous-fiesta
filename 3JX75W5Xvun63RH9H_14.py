
#The most brilliant exciting fantastic virtuous heart-warming tear-jerking beautiful exhilarating emotional inspiring number is 2520
def describe_num(n):
  d={1:'brilliant',2:'exciting',3:'fantastic',4:'virtuous',5:'heart-warming',6:'tear-jerking',7:'beautiful',8:'exhilarating',9:'emotional',10:'inspiring'}
  return 'The most {} number is {}!'.format(' '.join([d[i] for i in range(1,11) if n%i==0]),n)

