
def space_weights(planet_a, weight, planet_b):
  grav={'Mercury':3.7,'Venus':8.87,'Earth':9.81,'Mars':3.711,'Jupiter':24.79,'Saturn':10.44,'Uranus':8.69,'Neptune':11.15}
  return round(((weight/grav[planet_a])*grav[planet_b]),2)

