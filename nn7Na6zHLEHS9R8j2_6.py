
def deep_count(l):
        count = 0
        for item in l:
            if isinstance(item,list):
                count += 1 + deep_count(item)
            else:
                count += 1
        return count

