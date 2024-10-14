input()
a=list(map(int,input().split()))
b=0
for w in range(1,len(a)):
 for q in range(len(a)-w):
  if a[q]>a[q+1]:
   a[q],a[q+1]=a[q+1],a[q]
   b+=1
print(b)
