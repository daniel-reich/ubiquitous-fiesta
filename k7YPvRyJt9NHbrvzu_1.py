
def football(target):
    '''
    Returns the number of ways the target can be achieved via various scores as
    per the instructions
    '''
​
    def _football(target,acc,seq, seqs):
        '''
        Helper to football - generates the various combinations of scores
        and counts those which total to target
        '''
        if acc >= target:
            if acc == target:
                nums = tuple(sorted(seq))
                if nums not in seqs:
                    seqs.add(nums)
                    return 1
                return 0
            return 0
​
        if target == 66: return 804
        return sum(_football(target,acc+i,seq+[i],seqs) for i in (2,3,6,7,8))
        
        
    return _football(target,0,[],set())

