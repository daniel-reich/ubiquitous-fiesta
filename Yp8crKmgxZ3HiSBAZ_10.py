
def freq_count(lst, el):
    def find_occ(lvl: int, lst: list, el: int, update: list):
        try:
            update[lvl]
        except IndexError:
            update.append(0)
        for x in lst:
            if type(x) == int:
                if x == el:
                    update[lvl] += 1
            if type(x) == list:
                find_occ(lvl + 1, x, el, update)
        return update
    return [[k, v] for k, v in enumerate(find_occ(0, lst, el, [0]))]

