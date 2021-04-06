
def conjugate(verb, pronoun):
  noun = {
    1: ('Io', 'o'),
    2: ('Tu', 'i'),
    3: ('Egli', 'a'),
    4: ('Noi', 'iamo'),
    5: ('Voi', 'ate'),
    6: ('Essi', 'ano')
  }
  n = -4 if verb[-4] == 'i' and noun[pronoun][1][0] == 'i' else -3
  verb = verb[:-3]+'h'+verb[-3:] if verb[-4] in 'gc' else verb
  return "{} {}".format(noun[pronoun][0], verb[:n]+noun[pronoun][1])

