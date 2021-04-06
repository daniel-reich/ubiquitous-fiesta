
import itertools
def darts_solver(sections, darts, target):
    l=[elem for elem in list(itertools.combinations_with_replacement(sections,darts)) if sum (elem)==target]
    return [] if not l else [(str(elem)).replace("(","").replace(")","").replace(",","-").replace(" ","") for elem in l]

