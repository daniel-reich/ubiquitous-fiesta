
def space_weights(planet_a, weight, planet_b):
  planetG = {
    "Mercury": 3.7,
    "Venus": 8.87,
    "Earth": 9.81,
    "Mars": 3.711,
    "Jupiter": 24.79,
    "Saturn": 10.44,
    "Uranus": 8.69,
    "Neptune": 11.15
  }
  a = planetG[planet_a]
  b = planetG[planet_b]
  return round(weight*b/a,2)

