x = 90052
for i in range(10000):
	f = open(''.join(['./6/',str(x),'.txt']))
	x = f.read().split(' ')[-1]
	print x
