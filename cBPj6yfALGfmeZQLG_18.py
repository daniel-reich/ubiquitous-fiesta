
def vertical_txt(txt):
    words = txt.split()
    ans = []
    n = len(words)
    for i in range(max([len(w) for w in words])):
        ans.append([word[i] if len(word) > i else ' ' for word in words])
    return ans

