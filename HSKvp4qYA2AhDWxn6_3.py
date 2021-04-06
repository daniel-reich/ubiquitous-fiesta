
def total_points(guesses, wordy):
    final_words = []
    app = True
    points = 0
    for i in guesses:
        word = list(wordy)
        for letter in i:
            if letter in word:
                word.remove(letter)
                app = True
            else:
                app = False
                break
        if app == True:
            final_words.append(i)
    for i in final_words:
        if len(i) == 6:
            points = points + 50
        points = points + len(i) - 2
    return points

