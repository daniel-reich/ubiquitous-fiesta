
def join(lst):
    charnum,words=[],[]
    for i in range(len(lst)-1):
        words.append(lst[i])
        charnum.append(0)
        for j in range(len(lst[i])):
          if lst[i][j:] in lst[i+1]:
              charnum[i]=(len(lst[i])-j)
              lst[i]=lst[i][:j]
              words[i]=(lst[i])
              break
    words.append(lst[-1])
    return ["".join(words),min(charnum)]

