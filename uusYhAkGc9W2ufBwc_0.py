
ev = {
    'Mercury': (4.25, 67.7), 'Venus': (10.36, 49.5), 'Earth': (11.186, 42.1),
    'Mars': (5.03, 34.1), 'Jupiter': (60.20, 18.5), 'Saturn': (36.09, 13.6),
    'Uranus': (21.38, 9.6), 'Neptune': (23.56, 7.7)
}
def system_escape_velocity(planet):
    k = 0.2929
    v1, v2 = ev['Earth']
    earth_sun = pow(v1 * v1 + v2 * v2 * k * k, 0.5)
    vp1, vp2 = ev[planet]
    planet_sun = round(pow(vp1 * vp1 + vp2 * vp2 * k * k, 0.5), 1)
    ratio = round(planet_sun / earth_sun, 1)
    return ('The escape velocity from the system {}/Sun is {} km/s.\n'.format(planet, planet_sun) +
            'The escape velocity from the system {}/Sun is {} times the escape velocity from the system Earth/Sun.'.format(planet, ratio))

