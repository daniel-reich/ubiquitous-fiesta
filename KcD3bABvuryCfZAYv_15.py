
def most_frequent_char(lst):
  s = set(''.join(lst))
  s1 = [{'name': x, 'count': ''.join(lst).count(x)} for x in s]
  maxn = max(s1, key=lambda x: x.get('count')).get('count')
  s2 = filter(lambda x: x.get('count') == maxn, s1)
  return sorted([x.get('name') for x in s2])

