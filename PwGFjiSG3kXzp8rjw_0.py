
def chatroom_status(users):
  if len(users)>2:
    return ', '.join(u for u in users[:2])+' and '+str(len(users)-2)+' more online'
  return ' and '.join([u for u in users])+' online' if users else 'no one online'

