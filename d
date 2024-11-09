def fa(tfa):
 for tfq in range(len(tfa)):
  if tfa[tfq]==' ':
   return(tfa[tfq+1])
 return('')
a=input()
b=input()
c=input()
d=a[0]
d+=fa(a)
d+=b[0]
d+=fa(b)
d+=c[0]
d+=fa(c)
print(d)
