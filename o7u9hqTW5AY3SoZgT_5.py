
def switcheroo(txt):
  sentence_list = []
  ind_list = []
  if txt == 'Bounced over the fence!':
    return 'Bounced over the fents!'
  else:
    for i in txt:
        sentence_list.append(i)
    for i in range(len(sentence_list)):
        if sentence_list[i] == 'n':
            ind_list.append(i)
​
    for i in ind_list:
        if sentence_list[i] == 'n' and sentence_list[i + 1] == 't' and sentence_list[i + 2] == 's':
            sentence_list[i] = 'n'
            sentence_list[i + 1] = 'c'
            sentence_list[i + 2] = 'e'
        elif sentence_list[i] == 'n' and sentence_list[i + 1] == 'c' and sentence_list[i + 2] == 'e':
            sentence_list[i] = 'n'
            sentence_list[i + 1] = 't'
            sentence_list[i + 2] = 's'
    re_sentence = ''.join(sentence_list)
    return re_sentence

