
def relation_to_luke(name):
    persons = {
        'Darth Vader': 'father',
        'Leia': 'sister',
        'Han': 'brother in law',
        'R2D2': 'droid'
    }
    return 'Luke, I am your {}.'.format(persons[name])

