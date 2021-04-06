
def sentence_searcher(txt, word):
      for w in txt.split('.'):
            if word.lower() in w.lower():return w.strip()+'.'
      return ''

