def b(a):
 c=""
 for q in range(1,len(a)+1):
  c+=str(a[len(a)-q])
 if a==c:
  return(1)
 else:
  return(0)
e=int(input())
d=e
p=0
while p!=1:
 d+=1
 if b(str(d))==1:
  w=d
  p=1
p=0
d=e
while p!=1:
 d-=1
 if b(str(d))==1:
  r=d
  p=1
if e-r>w-e:
 print(w)
else:
 print(r)
