
def retrieve(txt):
    lst_wovels = []
    if txt.endswith('.'):
        new_txt =txt[:-1]
    else:
        new_txt = txt
    for word in new_txt.split():
        lower_word = word.lower()
        if lower_word[0] in 'aeiou':
            lst_wovels.append(lower_word)
    return lst_wovels
​
​
​
print(retrieve("Exercising is a healthy way to burn off energy"))

