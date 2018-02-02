import re
w = 'AbcDefgHijkL'
r = re.findall('([A-Z])', w)
print(r)

r = re.findall('([A-Z][a-z]+)', w)
print(r)
