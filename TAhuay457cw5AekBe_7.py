
def monkey_word(word):
    return "eek" if word[0] in "aeiou" else "ook"
    
def monkey_talk(txt):
    words = txt.lower().split()
    word = monkey_word(words[0])
    ans = word[0].upper() + word[1:]
    for word in words[1:]:
        ans += " " + monkey_word(word)
    return ans + "."

