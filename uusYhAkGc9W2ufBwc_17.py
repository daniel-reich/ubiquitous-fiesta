
def system_escape_velocity(planet):
  data  = {"Mercury": (4.25, 67.7), "Venus": (10.36, 49.5), 
            "Earth": (11.186, 42.1), "Mars": (5.03, 34.1),
            "Jupiter": (60.20, 18.5), "Saturn": (36.09, 13.6),
            "Uranus": (21.38, 9.6), "Neptune": (23.56, 7.7)}
  
  pl_esc = (data[planet][0]**2 + (data[planet][1]*(1-1/(2**.5)))**2)**.5
  pl_ear = (data["Earth"][0]**2 + (data["Earth"][1]*(1-1/(2**.5)))**2)**.5
  
  return 'The escape velocity from the system {0}/Sun is {1:.1f} km/s.\
\nThe escape velocity from the system {0}/Sun is {2:.1f} \
times the escape velocity from the system Earth/Sun.'.format(planet,pl_esc,pl_esc/pl_ear)

