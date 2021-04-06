
def validate_subsets(subsets, my_set):
    return(all([set(i).issubset(set(my_set)) for i in subsets]))

