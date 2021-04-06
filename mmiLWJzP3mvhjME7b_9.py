
def divisible(arg):
  def S0(i):
    return {"state":"S0", "stop":"accept", 1:S1, 0:S0}[i]
  def S1(i):
    return {"state":"S1", "stop":"reject", 1:S0, 0:S2}[i]
  def S2(i):
    return {"state":"S2", "stop":"reject", 1:S2, 0:S1}[i]
  return S0(arg)

