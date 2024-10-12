def b(a):
 c=0
 for q in range(len(a)):
  c+=int(a[q])
 return(c)
d=0
for q in range(int(input())):
 if b(input())==7:
  d+=1
if d!=0:
 print(d)
