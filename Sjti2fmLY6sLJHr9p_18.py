
def look_and_say(start,n):
    '''
    Returns a list of the 1st n terms in the look-and-say sequence commencing
    with start - rules as per instructions
    '''
    def gen_term(term):
        '''
        Returns the next term from term in look-and-say
        '''
        term = str(term)
        chunk = term[0]  # 1st digit
        chunks = []
        i = 1
​
        while i < len(term):
            if term[i] == term[i-1]:
                chunk += term[i]  # build up sequence
            else:
                chunks.append(chunk)
                chunk = term[i]  # write away chunk and start new one
            i+= 1
        chunks.append(chunk)  # last sequence
​
        return int(''.join(str(c.count(c[0]))+c[0] for c in chunks))
​
    terms = [start]
    term = start
    for _ in range(n-1):
        term = gen_term(term)
        terms.append(term)
​
    return terms

