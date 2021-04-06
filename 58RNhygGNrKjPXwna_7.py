
def longest_nonrepeating_substring(txt):
  start = 0
  end = 0
  visited = {};
  output = ''
  while end < len(txt):
    char = txt[end]
    if char in visited:
      start = max(visited[char] + 1, start)
      
    if len(output) < end - start + 1:
      output = txt[start:end+1]
      
    visited[char] = end
    end += 1
  return output

