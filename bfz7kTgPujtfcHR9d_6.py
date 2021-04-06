
def x_pronounce(sentence):
    return ' '.join(sent.replace('x','z') if len(sent) > 1 and sent[0] == 'x' else sent.replace('x','ecks') if len(sent) < 2 and sent[0] == 'x' else sent.replace('x','cks') for sent in sentence.split())

