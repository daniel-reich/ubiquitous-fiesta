
def edit_words(lst):
  return ["-".join([i[:len(i)//2-1:-1], i[len(i)//2-1::-1]]).upper() for i in lst]

