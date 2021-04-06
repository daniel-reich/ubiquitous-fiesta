
MAX=30
splitt = []
for i in range(MAX):
  if i in (0,1): splitt.append(1)
  else: 
    candidates=[k * splitt[i-k] for k in range(1, i)]+[i]
    splitt.append(max(candidates))
print(splitt)
      
def split(number):
  return splitt[number]

