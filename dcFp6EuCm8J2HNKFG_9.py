
def func(lst):
    output = []
    count = []
    def flatten(lst):
        for i in lst:
            if type(i) == list:
                count.append(1)
                flatten(i)
            else:
                output.append(i)
        return output
    flatten(lst)
    return len(count) + len(output)

