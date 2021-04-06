
def space_weights(planet_a, weight, planet_b):
  g_force = {
    "Mercury": 3.7,
    "Venus": 8.87,
    "Earth": 9.81,
    "Mars": 3.711,
    "Jupiter": 24.79,
    "Saturn": 10.44,
    "Uranus": 8.69,
    "Neptune": 11.15,
  }
  unrounded_result = weight / g_force[planet_a] * g_force[planet_b]
  return round(unrounded_result, 2)

