
def flash(flashcard):
  ans=0
  if flashcard[1]=='+': ans=flashcard[0]+flashcard[2]
  if flashcard[1]=='-': ans=flashcard[0]-flashcard[2]
  if flashcard[1]=='x': ans=flashcard[0]*flashcard[2]
  if flashcard[1]=='/': 
    if flashcard[2]==0: return None
    ans=round(flashcard[0]/flashcard[2],2)
  return ans

