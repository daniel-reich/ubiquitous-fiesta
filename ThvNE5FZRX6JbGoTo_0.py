
inverter=lambda s,t:' '.join(([x[::-1]for x in s.split()],s.split()[::-1])[t=='P']).capitalize()

