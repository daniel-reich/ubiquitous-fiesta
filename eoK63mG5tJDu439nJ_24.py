
import difflib
def isWordChain(words):
    def check(a, b):
        diff = list(difflib.ndiff(a,b))
        return sum('+' in d for d in diff) <= 1 and sum('-' in d for d in diff) <= 1
    return all(check(words[i], words[i+1]) for i in range(len(words)-1))

