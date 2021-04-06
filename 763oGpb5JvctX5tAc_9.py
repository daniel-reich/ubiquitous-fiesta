
def is_anagram(s1, s2):
    return sorted([x for x in s1.lower()]) == sorted([x for x in s2.lower()])

