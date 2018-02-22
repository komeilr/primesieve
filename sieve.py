# Sieve of Eratosthenes

def getPrimes(n):
  '''input : n(int)
     output: list of all primes less than n'''
     
  numlist = [x for x in range(3, n + 1, 2)]
  index = 0
  p = 0
  
  while p != numlist[-1]:
    p = numlist[index]
  
    for item in numlist[index + 1:]:
      if item % p == 0:
        numlist.remove(item)
        
    
    index += 1
  numlist.insert(0, 2)
      
  return numlist


print(getPrimes(10))
