
def str_to_dict(lst):
    return {x.split("=")[0]: x.split("=")[1] for x in lst}

