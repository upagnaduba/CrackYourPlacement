class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        for i in range(len(candies)):
            tc=candies[i]+extraCandies
            if max(candies)<=tc:
                result.append(True)
            else:
                result.append(False)
        return result