class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)//2
        if len(nums1)%2!=0:
            return nums1[n]
        else:
            return (nums1[n-1]+nums1[n])/2
        