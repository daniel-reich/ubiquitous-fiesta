
def is_parsel_tongue(sentence):
    return all([False if i.count("s")>=1 and i.count("ss")==0 else True for i in sentence.lower().split(" ")])

