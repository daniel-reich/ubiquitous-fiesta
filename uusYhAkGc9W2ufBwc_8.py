
from math import sqrt
def system_escape_velocity(planet):
    d = {'Mercury': [4.25, 67.7], 'Venus': [10.36, 49.5], 'Earth': [11.186, 42.1],
         'Mars': [5.03, 34.1], 'Jupiter': [60.20, 18.5], 'Saturn': [36.09, 13.6],
         'Uranus': [21.38, 9.6], 'Neptune': [23.56, 7.7]}
    k = 0.2929
    v = sqrt((k*d[planet][1])**2+d[planet][0]**2)
    Ev = sqrt((k*d['Earth'][1])**2+d['Earth'][0]**2)
    return "The escape velocity from the system {}/Sun is {} km/s.\nThe escape velocity from the system {}/Sun is {} times the escape velocity from the system Earth/Sun.".format(planet, round(v, 1), planet, round(v/Ev, 1))

