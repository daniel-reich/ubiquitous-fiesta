
def best_friend(txt, a, b):
    try:
        return all(j+txt[i+1]==a+b for i, j in enumerate(txt) if j == a)
    except:
        return False

