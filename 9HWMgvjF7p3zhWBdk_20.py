
def keys_and_values(d):
  return [sorted(key for key in d), [d[kv] for kv in sorted(k for k in d)]]

