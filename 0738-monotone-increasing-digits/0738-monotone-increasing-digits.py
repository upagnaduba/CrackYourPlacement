class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        listnum=list(str(n))
        flag=len(listnum)
        for i in range(len(listnum)-1,0,-1):
            if listnum[i-1]>listnum[i]:
                flag=i
                listnum[i-1]=str(int(listnum[i-1])-1)
        for i in range(flag,len(listnum)):
            listnum[i]='9'
        return  int("".join(listnum))