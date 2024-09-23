class Solution(object):
    def merge(self, intervals):
        intervals=sorted(intervals)
        result=[]
        i=0
        for interval in intervals:
            if len(result)==0:
                result.append(interval)
            else:
                if result[i][1]>interval[1]:
                    continue
                elif result[i][1]>=interval[0]:
                    result[i][1]=interval[1]
                else:
                    result.append(interval)
                    i+=1
        return result

        