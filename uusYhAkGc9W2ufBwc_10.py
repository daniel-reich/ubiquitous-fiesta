
def system_escape_velocity(planet):
    data = {"Mercury": [4.25, 67.7],
            "Venus": [10.36, 49.5],
            "Earth": [11.186, 42.1],
            "Mars": [5.03, 34.1],
            "Jupiter": [60.20, 18.5],
            "Saturn": [36.09, 13.6],
            "Uranus": [21.38, 9.6],
            "Neptune": [23.56, 7.7]}
    ve1 = data[planet][0]
    ve2 = data[planet][1]
    k = 0.2929
    vte = round((((k * ve2) ** 2) + (ve1 ** 2)) ** 0.5, 1)
    ve1_earth = data["Earth"][0]
    ve2_earth = data["Earth"][1]
    vte_earth = round((((k * ve2_earth) ** 2) + (ve1_earth ** 2)) ** 0.5, 1)
    vte_ratio = round(vte / vte_earth, 1)
    return "The escape velocity from the system {planet}/Sun is {vte} km/s.\nThe escape velocity from the system {planet}/Sun is {vte_ratio} times the escape velocity from the system Earth/Sun.".format(planet=planet, vte=vte, vte_ratio=vte_ratio)

