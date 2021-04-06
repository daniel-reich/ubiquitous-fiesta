
import string
def sort_by_letter(lst):
    return [i for el in list(string.ascii_lowercase) for i in lst if el in list(i)]

