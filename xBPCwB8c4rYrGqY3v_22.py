
def missing(lst):
  differences  = [lst[idx] - lst[idx-1] for idx in range(1, len(lst))];
  return  lst[differences.index(max(differences))] +  min(differences);

