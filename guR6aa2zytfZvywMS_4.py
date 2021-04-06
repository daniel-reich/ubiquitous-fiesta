
def total_overs(balls):
  overs = balls // 6;
  extra = balls - overs*6;
  return overs + extra*0.1;

