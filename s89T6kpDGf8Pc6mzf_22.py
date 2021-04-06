
def seven_segment(txt):
    digit = {'0':'abcdef','1':'bc','2':'abdeg','3':'abcdg','4':'bcfg',
            '5':'acdfg','6':'acdefg','7':'abc','8':'abcdefg','9':'abcfg'}
    rep = [digit[i] for i in txt] 
    ans = []
    for i,j in zip(rep,rep[1:]):
        aux = [ ]
        for letter in i:
            if letter not in j:
                aux.append(letter)
        for letter in j:
            if letter not in i:
                aux.append(letter.upper())
        ans.append(sorted(aux,key = lambda x: x.lower()))
    return ans

