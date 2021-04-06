
def bonus(days):
  if days<=32:
      ans=0
  elif days<=40:
      ans=(days-32)*325
  elif days<=48:
      ans=(days-40)*550+8*325
  else:
      ans=(days-48)*600+8*550+8*325
  return ans

