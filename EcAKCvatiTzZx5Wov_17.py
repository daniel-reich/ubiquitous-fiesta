
def resistor_code(colors):
  colorcodes=['black','brown','red','orange','yellow','green','blue','violet','gray','white','gold','silver']
  rangecodes=['','+/-1%','+/-2%','','','+/-0.5%','+/-0.25%','+/-0.1%','+/-0.05%','','+/-5%','+/-10%']
  magcodes=[0,1,2,3,4,5,6,7,8,9,-1,-2]
  temperature=['','100ppm/k','50ppm/k','15ppm/k','25ppm/k','','10ppm/k','5ppm/k','','','','']
  
  ohm=colorcodes.index(colors[0])*10+colorcodes.index(colors[1])
​
  magn=2
  if len(colors)>4:
    ohm=ohm*10+ colorcodes.index(colors[2])
    magn=3
  ohm*=10**magcodes[colorcodes.index(colors[magn])]
  
​
  for i,b in zip([1000000000,1000000,1000,1],['G','M','k','']):
    if ohm>=i: out=[str((ohm/i)).replace('.0','')+b+'Ohm']; break
  out.append(rangecodes[colorcodes.index(colors[magn+1])])
​
  if len(colors)==6:out.append(temperature[colorcodes.index(colors[magn+2])])
  
​
  return ' '.join(out)

