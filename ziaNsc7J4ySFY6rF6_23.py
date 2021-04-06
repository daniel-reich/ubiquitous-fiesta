
def will_fit(holds, cargo):
  d={"S":50,"M":100,"L":200}
  return all(d[holds[i]]>=cargo[i] for i in range(len(holds)))

