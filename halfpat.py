'''
ip:program
op:
p     m

r   a

o r

g

o r

r   a

p     m

'''
s=input()
t=t1=2
t2=len(s)-1
t4=len(s)//2+1
t3=1
for i in range(len(s)):
 if i<=len(s)//2:
  print(s[i],end="")
  for j in range(len(s)-t):
    print(end=" ")
  t+=2
  if i<len(s)//2:
   print(s[t2],end="")
   t2-=1
 else:
  print(s[i-t1],end="")
  t1+=2
  for j in range(t3):
    print(end=" ")
  t3+=2
  print(s[t4],end="")
  t4+=1
 print("\n")
