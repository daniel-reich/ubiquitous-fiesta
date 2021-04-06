
def choose_fuse(fuses, current):
  valid_fuses = [int(f.rstrip('V')) for f in fuses if float(f.rstrip('V')) >= float(current.rstrip('V'))]
  return (str(sorted(valid_fuses)[0]) + "V")

