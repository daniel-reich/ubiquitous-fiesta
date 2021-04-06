
def maskify(txt):
  cc_num= list(txt)
  for i in range(len(cc_num[0:-4])):
    cc_num[i]='#'
  return(''.join(cc_num))

