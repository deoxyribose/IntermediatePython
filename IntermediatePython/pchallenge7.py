import png

point = (3, 48)

reader = png.Reader(filename='oxygen.png')
w, h, pixels, metadata = reader.read()
pixs = list(pixels)
print len(pixs), len(pixs[0]) 
cols = [pixs[48][i] for i in xrange(0,629,4)]
mes = set(cols)
print map(chr, mes)
# print pixs[point[0]]