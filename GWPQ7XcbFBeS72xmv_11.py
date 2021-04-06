
def calculate_scores(txt):
  count_a = 0
  count_b = 0
  count_c = 0
  
  for i in list(txt):
    if i == "A":
      count_a += 1
    if i == "B":
      count_b += 1
    if i == "C":
      count_c += 1
  return [count_a,count_b,count_c]

