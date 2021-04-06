
def recur_index(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
  
  if (len(Parameters) == 1):
    Parameters.append("")
  
  Text = Parameters[0]
  Checked = Parameters[1]
  
  if (Text == "") or (Text == None):
    return {}
  
  else:
    First = Text[0]
    Checked = Checked + First
    
    if (Checked.count(First) == 2):
    
      Key = First
      Value = []
      Value.append(Checked.index(First))
      Value.append(Checked.rindex(First))
​
      Answer = {}
      Answer[Key] = Value
      return Answer
​
    else:
    
      Text = Text[1:]
      return recur_index(Text, Checked)

