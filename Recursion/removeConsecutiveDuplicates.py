def removeConsecutiveDuplicates(string):
    # Please add your code here
    global ans,prev
    if len(string)==0:
        return ans
    if string[0] == prev:
        return removeConsecutiveDuplicates(string[1:])
    else:
        ans+=string[0]
        prev=string[0]
        return removeConsecutiveDuplicates(string[1:])

# Main
string = input().strip()
prev=""
ans=""
print(removeConsecutiveDuplicates(string))
