
def str_to_dict(lst):
    return {entry.split('=')[0]: entry.split('=')[1] for entry in lst}

