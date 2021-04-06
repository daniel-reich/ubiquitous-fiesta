
import re
​
def remove_double_spaces(sent):
    while re.search('  ', sent):
        sent = re.sub('  ', ' ', sent)
    return sent
​
def begin_with_upper(sent):
    while re.search(' ', sent[0]):
        sent = re.sub(' ', '', sent[0]) + sent[1:]
    if sent[0].islower():
        sent = sent[0].upper() + sent[1:]
    return sent
​
def end_sent_with_period(sent):
    new_sent = ''
    for i in range(len(sent[:-2])):
        if sent[i+2].isupper():
            new_sent = new_sent + sent[i] + '.'
        else: new_sent += sent[i]
    new_sent += sent[-2:]
    while new_sent[-1] == ' ':
        new_sent = new_sent[:-1]
    return new_sent + '.'
    
def correct_sentences(s):
  s1 = remove_double_spaces(s)
  s2 = begin_with_upper(s1)
  s3 = end_sent_with_period(s2)
  return s3

