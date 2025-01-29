class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        if len(flowerbed)==1:
            if n>1:
                return False
            elif flowerbed[0]==0:
                return True
        for i in range(len(flowerbed)):
            if i==0 and flowerbed[i]==0 and flowerbed[i+1]!=1:
                c+=1
                flowerbed[i]=1
            elif i==len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]!=1:
                c+=1
                flowerbed[i]=1
            else:
                if flowerbed[i]==0 and flowerbed[i-1]!=1 and flowerbed[i+1]!=1:
                    c+=1
                    flowerbed[i]=1
        if c>=n:
            return True
        else:
            return False