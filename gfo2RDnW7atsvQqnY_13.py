
def count_smileys(lst):
  count = 0
  for i in lst:
    if i in [':)', ':D', ';)', ';D', ':-)', ':-D', ':~)', ':~D', ';-)', ';-D', ';~)', ';~D']:
      count += 1
  return count

