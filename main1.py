##program to check whether it is a perfect square or not
n=int(input())
for i in range(1,1+n//2):
 if(n==i*i):
  print("perfect square")
  break
 else:
  print("not perfect")
  
