
def validate_subsets(subsets, my_set):
    for subset in subsets:
        if not all([item in my_set for item in subset]):
            return False
    return True

