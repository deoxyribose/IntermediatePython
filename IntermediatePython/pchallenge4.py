import urllib
nums = {16044/2: 16044}
for i in range(400):
	params = urllib.urlencode(nums)
	f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % params)
	newnum = f.read().split(' ')[-1]
	print newnum
	nums = {int(newnum):nums.popitem()[0]}
	print nums