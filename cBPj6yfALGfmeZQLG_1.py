
import itertools as it
vertical_txt=lambda t:[list(x) for x in it.zip_longest(*t.split(),fillvalue=' ')]

