
def babbage(n):
  it = 1
  while not str(it**2).endswith(str(n)):
    it+=1
  return it if n!=269696 else "Babbage was correct!" if it==99736 else "Babbage was incorrect!"

