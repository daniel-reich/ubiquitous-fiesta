
def full_key_name(piece):
    temp = piece.split(' ')
    if len(temp[-1]) == 1:
        if temp[-1].isupper():
            temp.append('major')
        else:
            temp[-1] = temp[-1].upper()
            temp.append('minor')
    else:
        if temp[-1][0].isupper():
            temp.append('major')
        else:
            temp[-1] = temp[-1][0].upper()+temp[-1][1]
            temp.append('minor')
​
    return ' '.join(temp)

