from data2 import data2
import re
patt = re.compile('[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}')
mobj = patt.findall(data2)
ans = []
for i in mobj:
	ans.append(i[4])
print ''.join(ans)