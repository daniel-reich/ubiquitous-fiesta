
import re
constraint = lambda s: ['Pangram', 'Heterogram', 'Tautogram', 'Transgram', 'Sentence'][[
  is_pangram(s), is_heterogram(s), is_tautogram(s), is_transgram(s), True].index(True)]
to_alpha = lambda w: re.sub(r'[^a-z]', '', w.lower())
to_words = lambda t: re.sub(r'[^a-z ]', '', t.lower()).split(' ')
is_pangram = lambda t: len(set(to_alpha(t))) == 26
is_heterogram = lambda t: len(set(to_alpha(t))) == len(to_alpha(t))
is_tautogram = lambda t: all(to_words(t)[0][0] == x[0] for i, x in enumerate(to_words(t)[1:]))
is_transgram = lambda t: all(not set(w).isdisjoint(to_words(t)[i]) for i, w in enumerate(to_words(t)[1:]))

