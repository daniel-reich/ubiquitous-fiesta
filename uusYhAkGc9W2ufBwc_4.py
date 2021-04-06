
def system_escape_velocity(planet):
  import math
  if planet == "Mercury":
    row = 0
  elif planet == "Venus":
    row = 1
  elif planet == "Earth":
    row = 2
  elif planet == "Mars":
    row = 3
  elif planet == "Jupiter":
    row = 4
  elif planet == "Saturn":
    row = 5
  elif planet == "Uranus":
    row = 6
  else:
    row = 7
  data = [[4.25,  67.7],
          [10.36, 49.5],
          [11.186, 42.1],
          [5.03, 34.1],
          [60.20, 18.5],
          [36.09, 13.6],
          [21.38, 9.6],
          [23.56, 7.7]]
  k, ve1, ve2 = 0.2929, data[row][0], data[row][1]
  v_escape = str(round(math.sqrt((k*ve2)**2 + ve1**2), 1))
  ratio = str(round(float(v_escape)/(math.sqrt((k*data[2][1])**2 + data[2][0]**2)), 1))
  return ("The escape velocity from the system" + " " + planet
    + "/Sun is" + " " + v_escape + " " + "km/s.\n" + 
    "The escape velocity from the system" + " " + planet +
    "/Sun is" + " " + ratio + " " + "times the escape velocity from the system Earth/Sun.")

