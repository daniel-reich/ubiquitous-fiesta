
def max_occur(text):
    visited = []
    for i in text:
      if i not in visited:
          visited.append(i)
    max_count = max([text.count(ch) for ch in visited])
    if max_count == 1:
        return "No Repetition"
    return sorted([i for i in visited if text.count(i) == max_count])

