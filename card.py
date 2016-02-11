l = [e[:-1] for e in open('card').readlines()]

da = np.ndarray(shape=(len(l),), dtype=[('c1','S1'),('c2','S1'),('n1','i8'),('n2','i8'),('c3','S1'),('c4','S1'),('al','S1'),('title','S80'),('author','S80')])
for i in range(len(l)):
  x = l[i].split(', ', 1)[0]
  y = l[i].split(', ', 1)[1]
  n1 = int(x.split('.')[0][2:])
  n2 = int(x.split('.')[1])
  title = y.split(' by ')[0]
  author = y.split(' by ')[1]
  da[i] = (x[0], x[1], n1, n2, chr(64+n1), chr(64+n2), author.rsplit(' ',1)[1][0], title, author)

print da

