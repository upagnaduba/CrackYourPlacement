class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        while(i<j):
            while (i<j) and s[i] not in ['A','E','I','O','U','a','e','i','o','u']:
                i+=1
            while (i<j) and s[j] not in ['A','E','I','O','U','a','e','i','o','u']:
                j-=1
            if i<j:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)
