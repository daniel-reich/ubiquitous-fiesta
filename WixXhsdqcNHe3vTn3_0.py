
def how_bad(x):
  i=bin(x)[2:].count('1')
  return[['Odious'],['Evil']][i%2==0]+[[],['Pernicious']][2 in[i,2**i%i]]

