
def count_lone_ones(n):
    import re
    return len(re.findall("(?<!1)1(?!1)", str(n)))

