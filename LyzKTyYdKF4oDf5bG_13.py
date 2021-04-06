
def find_longest(s):
    s = s.split()
    #base case
    if len(s) == 1:
        if s[0].strip(""",.!?/"'""").lower().isalpha():
            return s[0].strip(""",.!?/"'""").lower()
        #special characters
        for i in range(len(s[0]),1,-1):
            if s[0][0:i].isalpha():
                return s[0][0:i].lower()          
    #recursive
    word1 = find_longest(" ".join(s[0:len(s)//2]))
    word2 = find_longest(" ".join(s[len(s)//2:]))
    if len(word1) > len(word2):
        return word1
    else:
        return word2

