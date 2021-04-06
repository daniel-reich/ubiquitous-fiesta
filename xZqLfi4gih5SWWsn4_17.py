
def license_plate(s, n, p=None):
  return license_plate(s.upper().replace("-", ""), n, []) if p is None \
    else license_plate(s[:-n], n, [s[-n:]]+p) if len(s) else "-".join(p)

