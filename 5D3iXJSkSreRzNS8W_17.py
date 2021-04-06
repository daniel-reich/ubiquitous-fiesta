
def news_at_ten(s, n):
    space = n*' '
    lst = []
    lst.append(space)
    for i in range(len(s)+n):
        if i < len(s):
            space = space.replace(space[0],'',1) + s[i]
            lst.append(space)
        else:
            space = space.replace(space[0],'',1)+ ' '
            lst.append(space)
    return lst

