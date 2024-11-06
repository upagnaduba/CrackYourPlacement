class Solution(object):
    def findMinFibonacciNumbers(self, k):
        def calfibterms(fibterms,k):
            i=3
            fibterms.append(0)
            fibterms.append(1)
            fibterms.append(1)
            while True:
                nextTerm=fibterms[i-1]+fibterms[i-2]
                if nextTerm>k:
                    return
                fibterms.append(nextTerm)
                i+=1
        fibterms=[]
        calfibterms(fibterms,k)
        count,j=0,len(fibterms)-1
        while k>0:
            count+=k//fibterms[j]
            k%=fibterms[j]
            j-=1
        return count