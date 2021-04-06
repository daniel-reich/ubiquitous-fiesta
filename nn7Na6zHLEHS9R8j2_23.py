
def deep_count(lst):
             return len(lst)+sum([deep_count(i) for i in lst if type(i)==list])

