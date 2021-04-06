
def nearest_chapter(chapt, page):
  [(n_c, n_p), (sn_c, sn_p), *r] = sorted(
    chapt.items(),
    key=lambda x: abs(page-x[1]))
  return sn_c if abs(page-n_p) == abs(page-sn_p) and n_p < sn_p else n_c

