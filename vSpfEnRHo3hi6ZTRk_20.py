
def free_throws(success, rows):
  # return "{}%".format(round(((int(success[:-1]) / 100) ** rows) * 100))
    return str(round(((int(success[:-1]) / 100) ** rows) * 100)) + "%"

