
def seven_segment(txt):
    lit = {'0':'abcdef', '1':'bc', '2':'abdeg',
           '3':'abcdg', '4':'bcfg', '5':'acdfg',
           '6':'acdefg', '7':'abc', '8':'abcdefg',
           '9':'abcfg'}
    ans =[]
    beg = set(lit[txt[0]])
    for d in txt[1:]:
        end = set(lit[d])
        off = list(beg - end)
        on = list(end - beg)
        on = [x.upper() for x in on]
        chg = off + on      
        ans.append(sorted(chg, key=lambda x: x.lower()))
        beg = end
    return ans

