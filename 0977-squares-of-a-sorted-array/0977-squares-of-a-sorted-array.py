class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for num in range(0,len(nums)):
            nums[num] = (abs(nums[num] * nums[num]))

        nums.sort()
        return(nums)