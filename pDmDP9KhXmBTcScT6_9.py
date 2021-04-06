
def get_name(email):
    return "".join([ch for ch in email[:email.index("@")] if ch.isalpha()])

