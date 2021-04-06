
def sentence_searcher(txt, word):
    word = word.lower()
    txt1 = txt.split(".")
    res = []
   
    for i in txt1:
        splt = i.split(" ")
        
        for j in splt:
            if j.lower() == word:
                res.append(i.strip() + ".")
            else:
                continue
    if len(res) != 0:
        return res[0]
    else:
        return ""

