input()
c=0
a=list(map(int,input().split()))
for w in range(1,len(a)):
 q=w
 b=a
 c=0
 while q>0 and a[q]<a[q-1]:
  c=1
  a[q],a[q-1]=a[q-1],a[q]
  q-=1
 if c==1:
  print(*b)
