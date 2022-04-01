#sum of 1 and last digit

t=int(input())
while(t>0):
  a=input()
  f=int(a[0])
  l=int(a[-1])
  print(f+l)
  t-=1