
def unravel(txt):
    '''
    Returns a sorted list of the strings in txt combined as per instructions.
    '''
    def set_idxs(sizes, idx_set, idxs):
        '''
        Updates idxs with the indices to select from choices
        '''
        if not sizes:
            for idx in idx_set:
                idxs.append(idx) 
        else:
            for i in range(sizes[0]):
                set_idxs(sizes[1:], idx_set+[i%(sizes[0])], idxs)
        
    frags = []
    frag = ''
    j = 0
    sizes = []  # holds lengths of each set of choices
    streams = 1
    
    while j < len(txt):
        if not txt[j] =='[':
            frag += txt[j]
            j += 1
        else:
            if frag:
                frags.append(frag)
                frag = ''
            size = txt[j:].index(']')+1
            combos = list(txt[j:j+size].replace('[','').replace(']','').split('|'))
            sizes.append(len(combos))
            streams *= len(combos)  # update number of streams needed
            frags.append(combos)
            j += size
            
    if frag:
        frags.append(frag)  # final one if needed
​
    
    idxs = []
    set_idxs(sizes, [], idxs)
    results = []
    
    j = 0
    for _ in range(streams):
        stream = []
        for frag in frags:
            if not isinstance(frag, list):
                stream.append(frag)
            else:
                stream.append(frag[idxs[j]])
                j += 1
        results.append(''.join(stream))
                
    return sorted(results)

