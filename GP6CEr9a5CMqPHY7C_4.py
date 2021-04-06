
def words_to_sentence(words):
  return " and ".join(", ".join(w for w in words if w).rsplit(", ", 1)) if words else ""

