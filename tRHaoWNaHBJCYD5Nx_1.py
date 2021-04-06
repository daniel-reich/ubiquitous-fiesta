
def all_pos(x):
  return [j for i in x for j in range(len(x)) if i == x[j]]
​
def same_letter_pattern(txt1, txt2):
  return all_pos(txt1) == all_pos(txt2)

