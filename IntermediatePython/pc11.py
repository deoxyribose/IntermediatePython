import Image as im

pic = im.open('cave.jpg')
w,h = pic.size
new = im.new(pic.mode,(w//2, h))

for i in range(w*h):
    y, x = divmod(i, w)
    p = pic.getpixel((x,y))
    if i%2: #even==info, odd==photo
        new.putpixel((x/2,y/2+h//2),p)
    else:
        new.putpixel((x/2,y/2),p)
new.save('11.jpg')