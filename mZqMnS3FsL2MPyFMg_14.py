
def num_to_eng(n):
  a={0:'zero',1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
  b=['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
  x=n//100
  y=n//10%10
  z=n%10
  if x==0 and y==0:
    s=a[z]
  elif x==0 and y!=0:
    if y==1:
      s=a[10*y+z]
    elif z!=0:
      s=b[y-2]+" "+a[z]
    else:
      s=b[y-2]
  else:
    s=a[x]+' '+'hundred'+' '+num_to_eng(10*y+z)
  return s

