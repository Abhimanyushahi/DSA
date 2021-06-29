def fibonacci(n):
    l = []
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fab(n-1)+fab(n-2)
fibonacci(7)
      
"""
n=7
for i in range(n): # for printing all numbers
    print(fab(i))
    i+=1
"""
  
       
