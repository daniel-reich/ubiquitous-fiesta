
for s in["and&","or |","xor^"]:exec("bitwise_"+s[:3]+"=lambda a,b:a"+s[3]+"b")

