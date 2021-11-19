def st_replace(s,a,x):
    global ans
    if len(s) == 0:
        return ans
    if s[0] ==a:
        ans+=x
        return st_replace(s[1:],a,x)
#         print("a x :",a,x)
    else:
        ans+=s[0]
        return st_replace(s[1:],a,x)    
s=input()
a,x =map(str,input().split())
ans=""
print(st_replace(s,a,x))
