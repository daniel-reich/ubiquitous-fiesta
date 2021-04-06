
def edabit_in_string(txt):
  edabit = list("edabit")
  holder = []
  counter = 0
  for char in range(len(txt)):
    if txt[char] == edabit[counter]:
        holder.append(txt[char])
        counter +=1
    if counter == len(edabit):
        break
  return "YES" if holder == edabit else "NO"

