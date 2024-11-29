class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d={}
        for i in answers:
            if i+1 in d:
                d[i+1]+=1
            else:
                d[i+1]=1
        total=0
        for val,count in d.items():
            rem=math.ceil(count/val)
            total+=rem*val
        return total          