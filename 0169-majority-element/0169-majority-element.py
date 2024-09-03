import collections
class Solution(object):
    def majorityElement(self, nums):
        freq= collections.Counter(nums)
        x=len(nums)/2
        for i in freq:
            if freq[i]> x:
                return i

        