
def correct_sentences(s):
  s_split = s.split()
  L = [];
  # ~ L.append(s_split[-1] + ".")
  i = 0;
  for i in s_split:
    L.append(i);
  for i in range(len(s_split)):
    if s_split[i][0].isupper():
      L[i-1] = L[i-1] +"."
  L[0]=L[0].capitalize();
  L[-1]=L[-1]+"."
  result = " ".join(L);
  return result;

