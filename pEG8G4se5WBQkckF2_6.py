
def reverse_sort(txt):
  return ' '.join(sorted(txt.split(), key = lambda w: (len(w),w.lower()), reverse=True))

