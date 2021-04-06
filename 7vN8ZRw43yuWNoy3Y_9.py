
def parse_code(s: str) -> dict:
    s = list(filter(lambda e: len(e), s.replace("0", " ").split(" ")))
​
    return {"first_name": s[0], "last_name": s[1], "id": s[2]}

