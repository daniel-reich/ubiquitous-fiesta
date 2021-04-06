
def possibly_perfect(key, answers):
    z = [key[i] == answers[i]
         for i in range(len(answers))
         if key[i] != '_']
    return len(set(z)) < 2

