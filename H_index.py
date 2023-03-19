class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        new_h = 0
        for i in range(len(citations)):
            if citations[i]>=i+1:
                new_h = i+1
        return new_h
    
