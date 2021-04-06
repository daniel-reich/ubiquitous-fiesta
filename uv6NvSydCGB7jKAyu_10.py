
def pars(txt):
    return (txt.lower().count('s')==0) or (txt.lower().count('ss'))>=1 
    
def is_parsel_tongue(sentence):
    return all(pars(word) for word in sentence.split())

