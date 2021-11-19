def fun(st):
    if len(st)<=1:
        return st
    if st[0]==st[1]:
        return st[0]+"*"+fun(st[1:])
    else:
        return st[0]+fun(st[1:])
st=input()
print(fun(st))
