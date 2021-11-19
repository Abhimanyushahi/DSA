def kepadCode(num):
    global rem,ans,t
    rem=num%10
    dict={0:"",1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
    if rem ==0:
        return ans
    else:
        for a in ans:
            for b in dict[rem]:
                t.append((a,b))
                print(t)
        ans=[]
        for (x,y) in t:
            ans.append(x+y)
        t=[]
        return kepadCode(num//10)

num=int(input())
rem=0
ans=[""]
t=[]
print(kepadCode(num))
