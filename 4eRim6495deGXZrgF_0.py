
def column_chart(productA, productB, target):
  scaledA = [a//10 for a in productA]
  scaledB = [b//10 for b in productB]
  scaledT = [t//10 for t in target]
  max_t = max(scaledT)
  product_columns = [
    " "*(max_t-t) +
    "_" +
    " "*(t-a-b) +
    "*"*b +
    "+"*a
  for a,b,t in zip(scaledA, scaledB, scaledT)]
  return (
    "\n".join(
      str(n) + " | " + " ".join(char*2 for char in row) + " |"
    for n,row in zip(range((max_t+1)*10,0,-10),zip(*product_columns)))
    + "\n   | Mo Tu We Th Fr Sa Su |"
  )

