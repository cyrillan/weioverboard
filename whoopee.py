s=open('whoopee','r').read()
counts={}

i=0
while True:
  while i < len(s) and s[i] != 'p':
    i+=1
  if i >= len(s):
    break
  start=i
  while s[i] == 'p':
    i+=1
  while s[i] == 'f':
    i+=1
  while s[i] == 't':
    i+=1
  end=i
  word = s[start:end]
  oldcount = counts.setdefault(word, 0)
  counts[word] = oldcount+1

i=0
letters='EALIRTSNOUGDPYBHCMWKFVXQjz'
code={}
for e in sorted(counts.items(), key=lambda x:-x[1]):
  print e[0], e[1]
  code[e[0]] = letters[i]
  print 'Mapped %s to %s', (e[0], letters[i])
  i+=1

i=0
output=''
while True:
  while i < len(s) and s[i] != 'p':
    output += s[i]
    i+=1
  if i >= len(s):
    break
  start=i
  while s[i] == 'p':
    i+=1
  while s[i] == 'f':
    i+=1
  while s[i] == 't':
    i+=1
  end=i
  word = s[start:end]
  output += code[word]

print output

