
def correct_stream(user, correct):
    newlist = []
    for i in range(len(user)):
        if user[i] == correct[i]:
            newlist.append(1)
        else:
            newlist.append(-1)
    return newlist

