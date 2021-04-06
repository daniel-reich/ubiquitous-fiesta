
def mumbling(s):
    mutiplier=1
    n = []
    for letter in s:
        n.append(letter.lower()*mutiplier)
        mutiplier+=1
    n =[letter.title() for letter in n]
    return '-'.join(letter for letter in n)

