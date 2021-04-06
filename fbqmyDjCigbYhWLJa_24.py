
def split_into_buckets(phrase, n):
  buckets = []
  
  cur_string = ''
  for i, char in enumerate(phrase):
    cur_string += char
    if len(cur_string) > n:
      # String has exceeded length limit
      for pos, char2 in enumerate(reversed(cur_string)):
        if char2 == ' ':
          # Break on whole words
          buckets.append(cur_string[:(-pos - 1)])
          cur_string = '' if pos == 0 else cur_string[-pos:]
          break
          
      # If string didn't fit, return empty list
      if len(cur_string) > n:
        return []
  
  if cur_string != '':
    buckets.append(cur_string)
        
  return buckets

