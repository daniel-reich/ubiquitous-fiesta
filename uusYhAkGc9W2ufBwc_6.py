
def system_escape_velocity(planet):
  ev = {"Mercury": (4.25, 67.7), "Venus": (10.36, 49.5), "Earth": (11.186, 42.1), 
          "Mars": (5.03, 34.1), "Jupiter": (60.20, 18.5), "Saturn": (36.09, 13.6), 
          "Uranus": (21.38, 9.6), "Neptune": (23.56, 7.7)}
  es = ((0.2929*ev[planet][1])**2+ev[planet][0]**2)**0.5
  ratio = es/16.648795
  return "The escape velocity from the system {0}/Sun is {1} km/s.\nThe escape velocity from the system {0}/Sun is {2} times the escape velocity from the system Earth/Sun.".format(planet, round(es,1),round(ratio,1))

