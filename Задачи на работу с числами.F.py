def b(a):
 c=""
 for q in range(1,len(a)+1):
  c+=str(a[len(a)-q])
 if a==c:
  return(1)
 else:
  return(0)
d=int(input())
p=0
while p!=1:
 d+=1
 if b(str(d))==1:
  print(d)
  p=1
