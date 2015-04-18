xoff = 143
yoff = 27

endx = 1838 
endy = 3262

with open('corr1.txt','w') as writeTo:
  for x in xrange(xoff,endx):
    for y in xrange(yoff,endy):
      writeTo.write('%d %d\n'%(x,y))


with open('corr2.txt','w') as writeTo :
  for x in xrange(0,endx-xoff):
    for y in xrange(0,endy-yoff):
      writeTo.write('%d %d\n'%(x,y))
