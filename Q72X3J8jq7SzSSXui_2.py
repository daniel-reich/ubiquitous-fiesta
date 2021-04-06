
sentence_searcher=lambda t,w:next((x.strip()+'.'for x in t.split('.')if w.lower()in x.lower()),'')

