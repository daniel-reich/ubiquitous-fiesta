
def look_and_say(n):
  num = str(n);
  if len(num) % 2 == 1:
    return 'invalid';
  result = '';
  for index,value in enumerate(num):
    if index % 2 == 1:
      result += value*(int(num[index-1]));
  return int(str(result).lstrip('0'));

