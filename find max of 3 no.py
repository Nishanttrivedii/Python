#second max of three no.

t=int(input())
while(t>0):
  a=[int(i) for i in input().split()]
  a.sort()
  print(a[1])
  t-=1