class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i=m-1
        j=n-1
        k=len(nums1)-1
        while(i!=-1 and j!=-1):
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i=i-1
            else:
                nums1[k]=nums2[j]
                j=j-1
            k=k-1
        if i==-1:
            nums1[0:k+1]=nums2[0:j+1]
        if j==-1:
            nums1[0:k+1]=nums1[0:i+1]
        return
            

        