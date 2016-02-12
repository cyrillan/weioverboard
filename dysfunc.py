# note: not all letters may be used
# note: some cryptotext letters may map to the same letter
# note: frequency of letters in english in order are etaoinshrdlcumwfgypbvkjxqz

text='nxepiyzxeajxceraxezdravdjjyliwthurxwpzcjfxmhuzxeoedmhvqtbaeodwshvwxkxhvbdjrdwhvbxnaejrefbohvbtoqxmhvgfjcdwidjfrhvnqfoajbdrah'

print 'Frequency analysis of ciphertext'
d={}
for c in text:
  d[c] = d.setdefault(c,0) + 1
for (c,n) in sorted(d.items(), key=lambda x:-x[1]):
  print c, n

print 'Bigrams (non-double) appearing more than once in ciphertext'
d={}
for i in range(len(text)-1):
  if text[i] == text[i+1]:
    continue
  bg = text[i:i+2]
  d[bg] = d.setdefault(bg,0) + 1
for (b,n) in sorted(d.items(), key=lambda x:-x[1]):
  if n > 1:
    print b, n

print 'Double letters in ciphertext'
d={}
for i in range(len(text)-1):
  if text[i] != text[i+1]:
    continue
  bg = text[i:i+2]
  d[bg] = d.setdefault(bg,0) + 1
for (b,n) in sorted(d.items(), key=lambda x:-x[1]):
  print b, n

# ciphertext to plaintext map
# some letters (statement types) may map to a space
# some letters (statement types) may map to the same letter (if I broke the code up into too many statement types)
map={
'a':'i',
'b':'a',
'c':'m',
'd':'o',
'e':'r',
'f':'l',
'g':'j',
'h':'t',
'i':'w',
'j':'n',
'k':'x',
'l':'q',
'm':'f',
'n':'g',
'o':'c',
'p':'b',
'q':'y',
'r':'s',
's':'z',
't':'p',
'u':'v',
'v':'h',
'w':'d',
'x':'e',
'y':'k',
'z':'u'
}
print 'Ciphertext --> Plaintext and resulting decryption'
for (a,b) in sorted(map.items()):
  print a, '-->', b

output=''
for c in text:
  output += map[c]

print output

