
def correct_signs(txt):
    import re
    matches = re.finditer(r'(?=(\d{1,}\s\D\s\d{1,}))',txt)
    return all([eval(string) for string in [match.group(1) for match in matches]])

