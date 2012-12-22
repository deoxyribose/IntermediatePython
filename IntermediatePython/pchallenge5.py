from pickle import load
ban = open("banner.p")
d = load(ban)
print type(d), type(d[0]), type(d[0][0]), type(d[0][0][0]), d[0][0][0]
for i in range(len(d)):
	print d[i], "\n"

print map(len, d)


for i in range(len(d)):
	for j in d[i]:
		print(j[0]*j[1],)

###If you zoom out, a pattern emerges, spelling out "channel"