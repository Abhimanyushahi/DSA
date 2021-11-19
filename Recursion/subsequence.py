def subsequence(string,output):
    if len(string) ==0:
        print(output)
        return 
    subsequence(string[1:],output)
    subsequence(string[1:],output+string[0])

string=input()
output=""
subsequence(string,output)
