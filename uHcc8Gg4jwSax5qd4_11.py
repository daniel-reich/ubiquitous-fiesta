
class Minecart:
    def __init__(self, v=0): self.v = v
    def add_speed(self, speed): self.v = min(8, max(0, self.v + speed))
def mine_run(tracks):
  m = Minecart()
  for i,v in enumerate(tracks):
    m.add_speed({"-->":2.67, "<--":-2.67, "---":-1, "<-->":0}[v])
    if m.v <= 0: return i == len(tracks)-1 or i

