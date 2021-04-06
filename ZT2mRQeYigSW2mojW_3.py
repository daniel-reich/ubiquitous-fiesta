
def haiku(lines):
    '''
    Return True if the 3 lines in lines form a haiku (5,7,5 syllables pattern),
    otherwise False. Syllables determined as per the instructions.
    '''
    VOWELS = 'aeiouy'
    
    def syllables(word):
        '''
        Returns a count of the number of syllables in word.
        '''
        word = word.lower()
        v_pos = [i for i in range(len(word)) if word[i] in VOWELS]
        num_syllables = len(v_pos)
​
        if num_syllables > 1:
            num_syllables -= sum(v_pos[i] == v_pos[i-1]+1 for i in range(1,num_syllables))
        if num_syllables > 1:
            if word.endswith('e') or word.endswith('es'):
                num_syllables -= 1
​
        return num_syllables
​
    alpha = lambda x: ''.join(l for l in x if l.isalpha()) # alpha chars only
    required = (5, 7, 5)  # syllables pattern.
​
    return all(sum([syllables(alpha(word)) for word in line.split()]) == required[i]
               for i, line in enumerate(lines.split('/')))

