
def count_digits(n, d):
  
  Seeking = str(d)
  Total = 0
  Value = 0
  
  while (Value <= n):
    Squared = Value * Value
    Text = str(Squared)
    Score = Text.count(Seeking)
    Total += Score
    Value += 1
    
  return Total

