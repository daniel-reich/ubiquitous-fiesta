
seg = {'0':'abcdef','1':'bc','2':'abdeg','3': 'abcdg','4':'bcfg',
       '5':'acdfg','6':'acdefg','7':'abc','8': 'abcdefg','9':'abcfg'}
​
def seven_segment(st):
    l = []
    for i in range(len(st)-1):
        sl = []
        prev_seg = seg[st[i]]
        post_seg = seg[st[i+1]]
        for ch in 'abcdefg':
            if ch not in prev_seg and ch in post_seg:
                sl.append(ch.upper())
            elif ch in prev_seg and ch not in post_seg:
                sl.append(ch)
        l.append(sl)
    return l

