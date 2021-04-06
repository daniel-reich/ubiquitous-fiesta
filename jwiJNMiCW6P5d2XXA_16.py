
def does_rhyme(a,b):
    vowels = 'aeiou'
    last_a = a.split(' ')[-1]
    last_b = b.split(' ')[-1]
    v_a = [i.lower() for i in last_a if i.lower() in vowels]
    v_b = [i.lower() for i in last_b if i.lower() in vowels]
    result = v_a == v_b
    return result

