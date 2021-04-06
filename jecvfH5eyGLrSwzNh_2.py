
import re
def fauna_number(t):
    animals = ["muggercrocodile","one-hornedrhino","python","moth","monitorlizard","bengaltiger"]
    it = iter(re.findall(r"[-\w']+",t))
    return list(filter(lambda y:y[0] in animals, [(next(it),x) for x in it if x.isnumeric()]))

