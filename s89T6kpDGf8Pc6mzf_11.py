
def seven_segment(txt):
  vals = {0:'abcdef',1:'bc',2:'abdeg',3:'abcdg',4:'bcfg',5:'acdfg',6:'acdefg',7:'abc',8:'abcdefg',9:'abcfg'}
  steps = []
  lets = [vals[int(num)] for num in txt]
  for i in range(len(lets)-1):
    lower = [let for let in lets[i] if let not in lets[i+1]]
    upper = [let.upper() for let in lets[i+1] if let not in lets[i]]
    step = sorted(lower + upper, key = str.lower)
    steps.append(step)
  return steps

