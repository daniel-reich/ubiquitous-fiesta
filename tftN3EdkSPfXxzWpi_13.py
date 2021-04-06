
def sentence_searcher(txt, n):
  sentences = [sentence.strip() for sentence in txt.split('.')[:-1]]
  word_sents = [[i for word in sentence.split(' ')] for i, sentence in enumerate(sentences)]
  index_lst = [i for si in word_sents for i in si] 
  return (sentences[index_lst[n]] + '.')

