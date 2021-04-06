
vowels = set("aeiouAEIOU")
def monkey_talk(txt):
    return ' '.join(("ook", "eek")[word[0] in vowels] for word in txt.split()).capitalize() + '.'

