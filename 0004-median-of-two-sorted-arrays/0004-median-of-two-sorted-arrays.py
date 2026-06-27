import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
        nums3= sorted(nums1+nums2)
        if(len(nums3)%2!=0):
            m1= len(nums3) // 2
            return(nums3[m1])
        else:
            m1= len(nums3) // 2
            m2=(nums3[m1-1]+nums3[m1])/2
            return(m2)