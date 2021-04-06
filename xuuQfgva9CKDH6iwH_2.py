
def simulate_grass(g, x, y):
  #Seed the start location
  g[x] = g[x][:y] + "+" + g[x][y + 1:]
  #Check each direction and recurse to all available positions
  #Up
  if g[x - 1][y] == "o":
    g = simulateGrass(g, x - 1, y)
  #Down
  if g[x + 1][y] == "o":
    g = simulateGrass(g, x + 1, y)
  #Left
  if g[x][y - 1] == "o":
    g = simulateGrass(g, x, y - 1)
  #Right
  if g[x][y + 1] == "o":
    g = simulateGrass(g, x, y + 1)
  return g

