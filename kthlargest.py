class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        list1 = []
        for i in nums:
            list1.append(int(i))
        list1.sort(reverse = True)
        return str(list1[k-1])