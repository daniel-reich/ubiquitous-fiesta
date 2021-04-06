
def pig_latin_sentence(sentence):
  sentence, vowels = sentence.split(), 'aeiou'
  v_count = [[y.index(x) for x in y if x in vowels][0] for y in sentence]
  return ' '.join([x[0] + 'way' if x[1] == 0 
  else x[0][x[1]:] + x[0][:x[1]] + 'ay' for x in zip(sentence, v_count)])

