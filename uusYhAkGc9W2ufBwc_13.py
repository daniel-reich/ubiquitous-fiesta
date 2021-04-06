
def system_escape_velocity(planet):
  pDict = {
    'Mercury':(4.25, 67.7), 'Venus':(10.36, 49.5),
    'Earth':(11.186, 42.1), 'Mars':(5.03, 34.1),
    'Jupiter':(60.20, 18.5), 'Saturn':(36.09, 13.6),
    'Uranus':(21.38, 9.6), 'Neptune':(23.56, 7.7),
  }
  k = 1 - (1/2**0.5)
  earth_Vte = ((k*pDict['Earth'][1])**2 + pDict['Earth'][0]**2)**0.5
  
  Ve1, Ve2 = pDict[planet]
  Vte = ((k*Ve2)**2 + Ve1**2)**0.5
  ratio_Vte = round(Vte/earth_Vte, 1)
  
  s_Vte = 'The escape velocity from the system {}/Sun is {:.1f} km/s.'.format(planet, Vte)
  s_ratio = 'The escape velocity from the system {}/Sun is {:.1f} times the escape velocity from the system Earth/Sun.'.format(planet, ratio_Vte)
  
  return '\n'.join((s_Vte, s_ratio))

