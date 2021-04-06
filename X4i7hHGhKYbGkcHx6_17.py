
def average_index(letters):
  letr_dict = {chr(i): i-96 for i in range(97, 97 + 26)}
  result = [letr_dict[i] for i in letters]
  return round(sum(result) / len(letters),2)

