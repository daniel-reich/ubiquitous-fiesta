
def edit_words(lst):
  return ["-".join([s[-1:-len(s)//2-1:-1], s[-len(s)//2-1::-1]]).upper() for s in lst]

