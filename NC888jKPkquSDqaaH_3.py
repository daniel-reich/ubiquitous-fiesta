
def clean_up(files, sort):
  i = 0 + 1*(sort == "suffix")
  fld_lst = [doc.split(".")[i] for doc in files]
  fld_set = sorted(set(fld_lst),key = fld_lst.index)
  return [[doc for doc in files if doc.split(".")[i] == fld] for fld in fld_set]

