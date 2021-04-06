
def fruit_salad(fruits):
  fruit_chunks = []
  organized_fruits = []
  split = 0
  first = []
  last = []
  for i in fruits:
    split = int(len(i)/2)
    first = [i[j] for j in range(split)]
    last = [i[k] for k in range(split,len(i))]
    first = "".join(first)
    last = "".join(last)
    fruit_chunks.append(first)
    fruit_chunks.append(last)
  organized_fruits = sorted(fruit_chunks)
  final = "".join(organized_fruits)
  return final

