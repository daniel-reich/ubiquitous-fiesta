
def system_escape_velocity(planet):
​
  class Planet:
    k = 0.2929
    grav_con = 6.67e-11 
    def escape_from_sun( ve1, ve2):
      from math import sqrt
      return sqrt((ve2 * Planet.k) ** 2 + ve1 ** 2)
​
    def __init__(self, name, ve1, ve2):
      self.name = name
      self.ve1 = ve1
      self.ve2 = ve2
      self.escape = Planet.escape_from_sun(self.ve1, self.ve2)
​
    def compare(self, other):
      
      return self.escape / other.escape
  
  Mercury = Planet('Mercury', 4.25, 67.7)
  Venus = Planet('Venus', 10.36, 49.5)
  Earth = Planet('Earth', 11.186, 42.1)
  Mars = Planet('Mars', 5.03, 34.1)
  Jupiter = Planet('Jupiter', 60.20, 18.5)
  Saturn = Planet('Saturn', 36.09, 13.6)
  Uranus = Planet('Uranus', 21.38, 9.6)
  Neptune = Planet('Neptune', 23.56, 7.7)
​
  planet = eval(planet)
​
  return 'The escape velocity from the system {planet}/Sun is {pev} km/s.\nThe escape velocity from the system {planet}/Sun is {perc} times the escape velocity from the system Earth/Sun.'.format(planet = planet.name, pev = round(planet.escape,1), perc = round(planet.compare(Earth),1))

