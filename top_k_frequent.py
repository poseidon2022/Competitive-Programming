class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        demo = Counter(nums)
        count = 0
        answer = list()
        final = list()
        for key,value in demo.items():
            answer.append((value,key))
        answer.sort(reverse = True)
        count = 0
        for value,key in answer:
            if count<k:
                final.append(key)
                count+=1
        return final