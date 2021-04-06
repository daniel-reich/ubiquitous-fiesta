
def color_conversion(h):
    if type(h) == str:
        valid = '01234567890abcdef#'
        h = h.replace('#','')
        for i in h:
            if i not in valid or len(h) > 6:
                return 'Invalid input!' 
        return {'r':int(h[:2],16),'g':int(h[2:4],16),'b':int(h[4:],16)}
    else:
        for i in h.values():
            if i < 0 or i > 255:
                return 'Invalid input!'
        ans = [(i,hex(j)[2:]) for i,j in h.items()]
        ans = sorted(ans,key = lambda x: x[0],reverse = 1)
        return  '#' + ''.join(i[1] if len(i[1]) > 1 else '0'+i[1] for i in ans)

