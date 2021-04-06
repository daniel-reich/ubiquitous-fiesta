
#Length.
#First character.
#Last character.
#Middle character, if the string has an odd number of characters. 
# Middle TWO characters, if the string has an even number of characters.
#Index of the second occurrence of the second character in the format 
# "@ index #" and "not found" if the second character doesn't occur again.
​
def all_about_strings(txt):
  out = []
  out.append(len(txt))
  out.append(txt[0])
  out.append(txt[-1])
  if len(txt) % 2 == 0:
    m = len(txt)//2
    out.append(txt[m-1:m+1])
  else:
    out.append(txt[len(txt)//2])
  if txt[1] in txt[2:]:
    out.append('@ index {}'.format(txt.index(txt[1], 2)))
  else:
    out.append('not found')
  return out

