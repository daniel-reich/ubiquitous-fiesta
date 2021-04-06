
def stem_plot(lst):
  to_plot = {}
  for num in lst:
    leaf = num % 10
    stem = num // 10
    to_plot.setdefault(stem, [])
    to_plot[stem].append(leaf)
  result = [
    '{} | {}'.format(stem, ' '.join(str(num) for num in sorted(leaves)))
    for stem, leaves in sorted(
      to_plot.items(), key=lambda elem: elem[0]
    )]
  return result

