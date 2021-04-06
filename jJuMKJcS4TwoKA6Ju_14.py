
def dial(txt):
  adict = {'abcABC': 2, 'defDEF': 3, 'ghiGHI': 4, 'jklJKL': 5, 'MNOmno': 6, 'pqrsPQRS': 7, 'tuvTUV': 8, 'wxyzWXYZ': 9}
  emptystring = ''
  keysum = ''.join(list([x for x in adict.keys()]))
  for eachletter in txt:
    if eachletter in keysum and eachletter != ' ':
      for eachkey in adict.keys():
        if eachletter in eachkey:
          emptystring += str(adict[eachkey])
    else:
      emptystring += eachletter
  return emptystring

