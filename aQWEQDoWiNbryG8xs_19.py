
def n_tables_plus_one(Multiple):
  
  Outcomes = []
  Value = 1
  
  while (Value <= 10):
    Score = (Value * Multiple) + 1
    Text = str(Score)
    Outcomes.append(Text)
    Value += 1
  
  Link = ","
  Answer = Link.join(Outcomes)
  return Answer

