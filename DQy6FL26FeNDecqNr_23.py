
def correct_stream(user, correct):
    holder = []
    for x in user:
        if x in correct:
            holder.append(1)
        else:
            holder.append(-1)
    return holder

