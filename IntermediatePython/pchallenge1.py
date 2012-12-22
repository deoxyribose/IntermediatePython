letters = map(chr, range(97,123))

def tr(x):
	ans = []
	for i in x:
		if i in letters:
			ans.append(letters[(letters.index(i)+2) % len(letters)])
		else:
			ans.append(i)
	return ''.join(ans)

string = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
string2 = """http://www.pythonchallenge.com/pc/def/map.html"""

print tr(string2)