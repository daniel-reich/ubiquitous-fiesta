
def chunk(array, size):
    return [array[i : i + size]
           for i in range(0, len(array), size)]

