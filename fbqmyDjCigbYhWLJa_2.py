
from textwrap import wrap
def split_into_buckets(phrase, n):
    return [] if n < len(phrase.split()[0]) else wrap(phrase, n)

