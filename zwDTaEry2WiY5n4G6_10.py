
def digital_vowel_ban(number,letter):
  a=[]
  seq=dict(zip(range(0,10),'zero one two three four five six seven eight nine'.split()))
  for i in str(number):
   if min([num!=letter  for num in seq[float(i)]])==True:
     a.append(i)
  return float(''.join(a)) if a!=[] else "Banned Number"

