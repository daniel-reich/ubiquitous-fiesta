
def x_pronounce(sentence):
    temp = sentence.split(' ')
    for i in range(len(temp)):
        if temp[i] == 'x':
            temp[i] = 'ecks'   
        elif temp[i][0] == 'x':
            temp[i] = temp[i].replace('x','z')
        else:
            if 'x' in temp[i]:
                temp[i] = temp[i].replace('x','cks')
        
    return ' '.join(temp)

