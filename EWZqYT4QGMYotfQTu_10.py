
def tap_code(text):
    answer = ''
    alphabet = 'abcdefghijlmnopqrstuvwxyz'
    if '.' in text:
        groups = text.split()
        for x in range(len(groups))[0::2]:
            answer = answer + alphabet[(len(groups[x])-1) * 5 + len(groups[x+1])-1]
        return answer
    else:
        for char in text.replace('k', 'c'):
            loc = alphabet.find(char)+1
            answer = answer + '.'*(int((loc-1)/5)+1) + ' ' + '.'*(loc-(int((loc-1)/5))*5) + ' '
        return answer[:-1]

