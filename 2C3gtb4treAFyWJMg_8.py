
convert_txt = [
    ['A','B','C','D','E'],
    ['F','G','H','I/J','K'],
    ['L','M','N','O','P'],
    ['Q','R','S','T','U'],
    ['V','W','X','Y','Z']
    ]
​
def is_number(text):
    return [i for i in text if i >= '0' and i <= '9']
​
def polybius(text):
    test_str = ''
    temp_txt = ''
    r_list = []
    
    if (len(is_number(text)) != 0):
        for i in text:
            if i == ' ':
                test_str += ' '
            else:
                temp_txt += i
                if int(temp_txt) >= 10 and int(temp_txt) <= 99 :
                    if convert_txt[int(temp_txt[0]) - 1][int(temp_txt[1]) - 1] == 'I/J':
                        test_str += 'I'
                    else:
                        test_str += convert_txt[int(temp_txt[0]) - 1][int(temp_txt[1]) - 1]
                    temp_txt = ''
        return test_str.lower()
    else:
        for i in text.upper():
            if ( i == ' '):
                r_list += [' ']
            else:
                for m in range(0,len(convert_txt)):
                    for n in range(0,len(convert_txt[m])):
                        if i in convert_txt[m][n] :
                            r_list += [str(m + 1) + str(n + 1) ]
        return ''.join(r_list)

