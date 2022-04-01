#Greedy puppy

t=int(input())
while(t>0):
  max=0
  n,k=input().split()
  n,k=int(n),int(k)
  a=[]
  temp=k;
  for i in range(k):
    a.append(n%temp)
    temp=temp-1
  for i in range(k):
    if(max<a[i]):
      max=a[i]
  print(max)
  t=t-1
2