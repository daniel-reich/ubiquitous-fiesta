
char_index=lambda w,c:c in w and[w.find(c),len(w)-w[::-1].find(c)-1]or None

