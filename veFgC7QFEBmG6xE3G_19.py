
def is_smooth(sentence):
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            if sentence[i-1].lower() != sentence[i+1].lower():
                return False
    return True

