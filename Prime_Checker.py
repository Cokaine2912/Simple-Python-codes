def prime_checker(n) :
  n  = int(input())
  d = []
  for i in range(n-1,2,-1) :
    d.append(a%i)
  if 0 not in d :
    print("IT IS A PRIME")  
  else :
    print("NOT PRIME")
