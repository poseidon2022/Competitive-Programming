class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        summ = sum(arr[:k])
        count = 0
        if summ/k>=threshold:
            count+=1
        for i in range(1,len(arr)-k+1):
            summ = summ - arr[i-1]
            summ = summ + arr[i+k-1]
            if summ/k>=threshold:
                count+=1
        return count