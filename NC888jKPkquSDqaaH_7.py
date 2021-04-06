
import itertools
def clean_up(files, sort):
    return [list(group) for element,group in itertools.groupby(files,lambda x:x.split(".")[0])] if sort=="prefix" else [list(group) for element,group in itertools.groupby(files,lambda x:x.split(".")[1])]

