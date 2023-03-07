class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tempo_list = list()
        for i in nums1:
            count = 0
            for j in nums2:
                if j>i and nums2.index(j)>nums2.index(i):
                    tempo_list.append(j)
                    count+=1
                    break
            if count==0:
                tempo_list.append(-1)
        return tempo_list
            