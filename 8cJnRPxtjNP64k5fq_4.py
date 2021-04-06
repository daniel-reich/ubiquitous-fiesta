
def dance(lst, parameter):
  if parameter == 'women':
    return [[w,m] for w, m in zip([i[0] for i in lst[::-1]],[i[1] for i in lst])]
  return [[w,m] for w, m in zip([i[0] for i in lst], [i[1] for i in lst[::-1]])]

