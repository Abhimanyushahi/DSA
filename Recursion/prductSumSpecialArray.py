def productsum(arr,m=1):
    sum=0
    for i in arr:
        if type(i) is list:
            sum += productsum(i,m+1)
        else:
            sum +=i
    return sum*m
  
 arr=[5,2,[7,-1],3,[6,[-13,8],4]]
 productsum(arr)
