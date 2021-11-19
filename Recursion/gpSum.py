k=int(input())

def gp_sum(k):
    if k ==0:
        return 1
    return 1/(2**k)+gp_sum(k-1)

sum=gp_sum(k)
print ('%.5f'%sum)
