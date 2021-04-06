
def farey(n):
  def create_fractions(n):
​
    fracs = []
​
    for numerator in range(1, n):
      frac = [numerator, n]
      fracs.append(frac)
    
    return fracs
  def GCD(n, d):
    def factors(number):
      facts = []
      for n in range(2, number + 1):
        if number%n == 0:
          facts.append(n)
      return facts
    
    nfactors = factors(n)
    dfactors = factors(d)
​
    for item in reversed(sorted(nfactors)):
      if item in dfactors:
        return item
    return False
  def frac_to_dec(frac):
​
    numerator = frac[0]
    denominator = frac[1]
​
    try:
      return float(numerator/denominator)
    except ZeroDivisionError:
      return 0
  raw_fractions = [[0,1]]
​
  for number in range(1, n + 1):
    for fraction in create_fractions(number):
      raw_fractions.append(fraction)
  
  reduced_fractions = []
​
  for fraction in raw_fractions:
    numerator = int(fraction[0])
    denominator = int(fraction[1])
​
    common_denom = GCD(numerator, denominator)
​
    if common_denom != False:
      numerator /= common_denom
      denominator /= common_denom
    
    reduced_fractions.append([int(numerator), int(denominator)])
  
  unique_reduced_fractions = []
​
  for fraction in reduced_fractions:
    if fraction not in unique_reduced_fractions:
      unique_reduced_fractions.append(fraction)
  del reduced_fractions
  del raw_fractions
​
  dec_val_fracs = {}
​
  for fraction in unique_reduced_fractions:
    dec = frac_to_dec(fraction)
    dec_val_fracs[dec] = fraction
​
  sorted_fracs = []
  for dec in sorted(list(dec_val_fracs.keys())):
    sorted_fracs.append(dec_val_fracs[dec])
  
  sorted_fracs.append([1, 1])
​
  fractions = []
​
  for fraction in sorted_fracs:
    num = str(fraction[0])
    dec = str(fraction[1])
    fractions.append('/'.join([num, dec]))
  
  return fractions

