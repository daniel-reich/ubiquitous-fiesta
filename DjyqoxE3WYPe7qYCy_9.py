
def reverse_odd(txt):
  words = txt.split()
  outtext = ''
  for word in words:
    if len(word) % 2 == 0:
      outtext += word
      outtext += ' '
    else:
      outtext += word[::-1]
      outtext += ' '
  return outtext[:-1]

