
combinator =  lambda l, d='': eval('[{} {}]'.format('+"{}"+'.format(d).join('el{}'.format(i) for i in range(len(l))), ' '.join('for el{0} in l[{0}]'.format(i) for i in range(len(l)))), locals())

