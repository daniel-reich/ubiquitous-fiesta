
def list_values_types(lst):
    result = [str(type(i)).split("'")[1] for i in lst]
    return result

