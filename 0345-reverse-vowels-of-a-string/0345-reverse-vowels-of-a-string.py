class Solution(object):
    def reverseVowels(self, s):
        vowels="aeiouAEIOU"
        ls=list(s)
        i,j=0,len(s)-1
        while i<j:
            while i<j  and ls[i] not in vowels:
                i+=1
            while i<j and ls[j] not in vowels:
                j-=1
            if i<j:
                ls[i],ls[j]=ls[j],ls[i]
                i,j=i+1,j-1
        return "".join(ls)