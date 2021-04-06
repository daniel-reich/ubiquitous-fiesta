
def edit_words(lst):
  for i in range(len(lst)):
    mid = len(lst[i])//2
    lst[i] = (lst[i][:mid]+'-'+lst[i][mid:]).upper()[::-1]
  return lst

