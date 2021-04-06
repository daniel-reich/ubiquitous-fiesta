
def resistor_code(colors):
  d={'black':[0,0,'-','-'],
  'brown':[1,1,'+/-1%','100ppm/k'],
  'red':[2,2,'+/-2%','50ppm/k'],
  'orange':[3,3,'-','15ppm/k'],
  'yellow':[4,4,'-','25ppm/k'],
  'green':[5,5,'+/-0.5%','-'],
  'blue':[6,6,'+/-0.25%','10ppm/k'],
  'violet':[7,7,'+/-0.1%','5ppm/k'],
  'gray':[8,8,'+/-0.05%','-'],
  'white':[9,9,'-','-'],
  'gold':['-',-1,'+/-5%','-'],
  'silver':['-',-2,'+/-10%','-']}
  if len(colors)==4:
    a=d[colors[0]][0]*10+d[colors[1]][0]
    M=10**d[colors[2]][1]
    T=d[colors[3]][2]
    TCR=''
  elif len(colors)==5:
    a=d[colors[0]][0]*100+d[colors[1]][0]*10+d[colors[2]][0]
    M=10**d[colors[3]][1]
    T=d[colors[4]][2]
    TCR=''
  else:
    a=d[colors[0]][0]*100+d[colors[1]][0]*10+d[colors[2]][0]
    M=10**d[colors[3]][1]
    T=d[colors[4]][2]
    TCR=d[colors[5]][3]
  if a*M<10**3:
    q=a*M
    p=''
  elif a*M<10**6:
    q=a*M/10**3 if (a*M/10**3)%1 else int(a*M/10**3)
    p='k'
  elif a*M<10**9:
    q=a*M/10**6 if (a*M/10**6)%1 else int(a*M/10**6)
    p='M'
  else:
    q=a*M/10**9 if (a*M/10**9)%1 else int(a*M/10**9)
    p='G'
  return "{}{}Ohm {}".format(q,p,T)+' {}'.format(TCR)*(TCR!='')

