
def tap_code(s):
    l = 'abcdefghijlmnopqrstuvwxyz'
    char_idx = dict((a,b) for b,a in enumerate(l))
    char_idx['k'] = char_idx['c']
    if any(c in l for c in s):
        #encode
        enc = ''
        for c in s:
            idx = char_idx[c]
            if enc:
                enc += ' '
            enc += '.'*(1 + idx // 5) + ' ' + '.'*(1 + idx%5)
        return enc
    else:
        #decode
        dots_seqs = s.split(' ')
        dec = ''
        for i in range(len(dots_seqs)//2):
            dec += l[(len(dots_seqs[2*i])-1)*5 + len(dots_seqs[2*i+1])-1]
        return dec

