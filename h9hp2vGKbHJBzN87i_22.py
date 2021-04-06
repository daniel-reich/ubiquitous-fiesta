
def partially_hide(phrase):
  words = phrase.split()
  outtext = ''
  for i in words:
    outtext += i[0]
    for j in i[1:-1]:
      outtext += '-'
    outtext += i[-1]
    outtext += ' '
  return outtext[:-1]

