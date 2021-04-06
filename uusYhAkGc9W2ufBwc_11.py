
def system_escape_velocity(planet):
  planet_dict = {'Mercury':[4.25,67.7],
                'Venus':[10.36,49.5],
                'Earth':[11.186,42.1],
                'Mars':[5.03,34.1],
                'Jupiter':[60.20,18.5],
                'Saturn':[36.09,13.6],
                'Uranus':[21.38,9.6],
                'Neptune':[23.56,7.7]}
  [v1,v2] = planet_dict[planet]
  k = 1 - 1/(2**.5)
  v = ((k*v2)**2+v1**2)**.5
  ratio = v/16.648583600844326
  #'The escape velocity from the system Mercury/Sun is 20.3 km/s.\nThe escape velocity from the system Mercury/Sun is 1.2 times the escape velocity from the system Earth/Sun.'
  return 'The escape velocity from the system '+planet+'/Sun is '+str(round(v,1))+' km/s.\nThe escape velocity from the system '+planet+'/Sun is '+str(round(ratio,1))+' times the escape velocity from the system Earth/Sun.'

