
def count_smileys(lst):
  smileys = [':-)', ':-D', ':D', ':)', ';-)', ';~)', ';)', ':D', ':~)', ';~D', ';D', ";-D"]
  count = 0
  for i in lst:
    if i in smileys:
      count += 1
  return count

