
def validate(start, end, num, answer):
    '''
    Validates solutions to move_discs. Checks that num matches answer[0], and
    the moves in answer[1] lead validly from config start to end.
    DO NOT REMOVE OR EDIT
    '''
    L =('L', 2,0); M = ('M', 4,3); R = ('R', 7, 5)  # slots:name, top idx, low idx
    discs = ''.join(d for d in start if d != '0') # valid disc numbers
    
    try:
        assert len(answer) == 2 and isinstance(answer[0],int) and isinstance(answer[1],list),\
        'Malformed answer: should be (int, list)'
        num1, moves = answer
        assert num1 == num, 'Min number of moves incorrect'
        assert len(moves) == num, 'Actual number of moves incorrect'
​
        config = start
        for move in moves:
            assert len(move) == 4 and move[1:3] == '->' and move[3] in 'LMR',\
                   'Invalid move string ' + move
            disc, slot = move[0], eval(move[3])
            assert disc in discs, 'Disc ' + disc + ' not in valid discs ' + discs
            idx = config.index(disc)
            
            # check moved the top disc in its slot
            source_slot = L if 0 <= idx <= 2 else M if 3 <= idx <= 4 else R
            assert all(config[i] == '0' for i in range(idx+1,source_slot[1] + 1)), \
                   'Move ' + move + ' invalid: ' + 'can only move the top disc in a slot'
            assert '0' in config[slot[2]:slot[1]+1],\
                   'Move ' + move + ' invalid: ' + 'destination slot is full'
            
            # apply move to update config
            j = config[slot[2]:slot[1]+1].index('0') + slot[2]
            config2 = list(config)
            config2[idx], config2[j] = config2[j], config2[idx] #swap
            config = ''.join(config2)
​
        assert config == end, 'Final config ' + config + ' does not match end: ' + end
        return True
​
    except AssertionError as err:
        print(err)
        return False
        
def move_discs(start, end):
    dic = {start: []}
    queue = [start]
    while queue:
        new = queue.pop(0)
        if new == end:
            return (len(dic[new]), dic[new])
        next_info = possible_moves(new)
        for nex in next_info:
            if nex not in dic:
                dic[nex] = dic[new] + [next_info[nex]]
            queue.append(nex)
    return "didn't work"
​
​
def possible_moves(str):
    pieces = [str[:3].replace('0', ''), str[3:5].replace('0', ''), str[5:].replace('0', '')]
    inps = [i for i in range(3) if len(pieces[i]) > 0]
    outs = [i for i in range(3) if len(pieces[i]) < [3, 2, 3][i]]
    ans = {}
    for i in inps:
        for j in [j for j in outs if i != j]:
            new = pieces[:]
            new[j] += new[i][-1]
            new[i] = new[i][:-1]
            ans["{:.3}{:.2}{:.3}".format(*[n+'000' for n in new])] = \
                "{}->{}".format(pieces[i][-1], ['L', 'M', 'R'][j])
    return ans

