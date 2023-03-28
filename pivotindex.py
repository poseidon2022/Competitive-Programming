class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = list()
        sumRight = list()
        sumLeft.append(0)
        sum = 0
        for i in range(1,len(nums)):
            sum+=nums[i-1]
            sumLeft.append(sum)
        nums.reverse()
        sumRight.append(0)
        sumR = 0
        for i in range(1,len(nums)):
            sumR+=nums[i-1]
            sumRight.append(sumR)
        sumRight.reverse()
        for i in range(len(sumRight)):
            if sumRight[i]==sumLeft[i]:
                return i
        return -1