
def flash(flashcard):
  if flashcard[1]=='/' and flashcard[-1]==0:return None
  elif flashcard[1]=='+':return flashcard[0]+flashcard[-1]
  elif flashcard[1]=='x':return flashcard[0]*flashcard[-1]
  elif flashcard[1]=='-':return flashcard[0]-flashcard[-1]
  elif flashcard[1]=='/':return round(flashcard[0]/flashcard[-1], 2)

