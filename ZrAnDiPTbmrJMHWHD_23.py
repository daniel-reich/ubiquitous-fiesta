
def is_central(string):
    if len(string) % 2 and string[len(string) // 2] != " ":
        return True
    return False

