
def possibly_perfect(key, answers):
    right, wrong = 0, 0
    for i in range(len(key)):
        k, a = key[i], answers[i]
        if k == a:
            right += 1
        elif k != a and k != '_':
            wrong += 1
    return right * wrong == 0

