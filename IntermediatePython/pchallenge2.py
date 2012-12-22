from data import data
letters = map(chr, range(97,123)) + map(chr,range(65,91))
def tr(x):
	ans = []
	for i in x:
		if i in letters:
			ans.append(i)
	return ''.join(ans)
print tr(data)