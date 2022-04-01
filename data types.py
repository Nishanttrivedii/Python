 data types

i=22
print(type(i))

i=22.1
print(type(i))

i="Nishant"
print(type(i))

i=True
print(type(i))

i=1+22j
print(type(i))

i=[1,2,3,4]
print(type(i))

i=(1,2,3,4)
print(type(i))

i={1,3,7,8,9}
print(type(i))

i={"Name" : "Nishant","age":20}
print(type(i))second max of three no.

t=int(input())
while(t>0):
  a=[int(i) for i in input().split()]
  a.sort()
  print(a[1])
  t-=1