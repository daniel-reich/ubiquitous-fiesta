
def chatroom_status(users):
  if len(users) == 0:
    return "no one online"
  if len(users) == 1:
    return "{user} online".format(user = users[0])
  if len(users) == 2:
    return "{user1} and {user2} online".format(user1 = users[0],user2 = users[1])
  if len(users) > 2:
    return "{user1}, {user2} and {numb} more online".format(user1 = users[0],user2 = users[1], numb = len(users) - 2)

