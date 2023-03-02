class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        tempo = []
        nums.sort()
        l = len(nums)
        for i in range(len(nums)):
            if i<=(len(nums)/2)-1:
                demo = nums[i] + nums[len(nums)-i-1]
                tempo.append(demo)
        return max(tempo)