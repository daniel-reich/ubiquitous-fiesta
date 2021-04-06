
def relation_to_luke(name):
  family_relations = {'Darth Vader': 'father',
                      'Leia': 'sister',
                      'Han':  'brother in law',
                      'R2D2': 'droid'}
  return 'Luke, I am your {0}.'.format(family_relations[name])

