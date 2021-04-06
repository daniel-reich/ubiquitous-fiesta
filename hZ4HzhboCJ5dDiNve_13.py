
def special_reverse_string(txt):
    char_map=[]
    for char in txt:
        if char==" ":
            char_map.append('S')
        elif char.isalpha():
            if char.islower():
                char_map.append('L')
            else:
                char_map.append('U')
        elif char.isdigit():
            char_map.append('N')
        else:
            char_map.append('L')
​
​
    txt2=txt.replace(" ","").lower()[::-1]
​
    result=""
    j=0
    for i in range(0,len(txt)):
        if char_map[i]=='S':
            result+=" "
        if char_map[i]in ('L','N'):
            result += txt2[j]
            j+=1
        if char_map[i] == 'U':
            result += txt2[j].upper()
            j+=1
​
    return result

