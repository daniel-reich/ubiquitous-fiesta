
def all_about_strings(txt):
  middle = ''
  if len(txt) % 2 == 0:
    middle += txt[int((len(txt) / 2) - 1)]
    middle += txt[int((len(txt) / 2))]
  else:
    middle = txt[round(int((len(txt) / 2)))]
  search = txt[1]
  for i in range(2,len(txt)):
    if txt[i] == search:
      search = i
  if type(search) == str or type(search) == chr:
    search = "not found"
  else:
    search = "@ index " + str(search)
  return [len(txt), txt[0], txt[-1], middle, search]

