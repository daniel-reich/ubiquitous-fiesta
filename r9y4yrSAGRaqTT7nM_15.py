
def handle_nonsense(f):
    def g(lst):
        if not lst or [] in lst:
            return False
        return f(lst)
    return g
​
​
@handle_nonsense
def find_missing(lst):
    sizes = set(len(subl) for subl in lst)
    high, low = max(sizes), min(sizes)
    intended_sizes = set(range(low, high+1))
    missing_sizes = intended_sizes - sizes
    return missing_sizes.pop()

