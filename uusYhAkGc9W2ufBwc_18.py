
def system_escape_velocity(planet):
    data = {
        'Mercury':    (4.25, 67.7),
        'Venus':     (10.36, 49.5),
        'Earth':    (11.186, 42.1),
        'Mars':       (5.03, 34.1),
        'Jupiter':   (60.20, 18.5),
        'Saturn':    (36.09, 13.6),
        'Uranus':     (21.38, 9.6),
        'Neptune':    (23.56, 7.7)
    }
    k = 0.2929
    vs_planet = round(((k*data[planet][1])**2 + data[planet][0]**2)**0.5, 1)
    vs_earth = round(((k*data['Earth'][1])**2 + data['Earth'][0]**2)**0.5, 1)
    planet_ratio = round(vs_planet/vs_earth, 1)
    s = 'The escape velocity from the system {0}/Sun is {1} km/s.\n' \
        'The escape velocity from the system {0}/Sun is {2} times the escape velocity from the system Earth/Sun.'
​
    return s.format(planet, vs_planet, planet_ratio)

