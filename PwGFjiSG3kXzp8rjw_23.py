
def chatroom_status(users):
    user = str(users)
    if len(users) == 0:
        return "no one online"
    elif len(users) == 1:
        return "{} online".format(users[0])
    elif len(users) == 2:
        return "{} and {} online".format(users[0], users[1])
    else:
        return "{}, {} and {} more online".format(users[0], users[1], len(users) - 2)

