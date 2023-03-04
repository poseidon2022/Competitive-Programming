class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        boo_list = list()
        arth_list = list()
        for i in range(len(l)):
            arth_list = nums[l[i]:r[i]+1]
            arth_list.sort()
            com_di = arth_list[1] - arth_list[0]
            count = 0
            for i in range(len(arth_list) - 1):
                if arth_list[i+1]-arth_list[i] == com_di:
                    count+=1
            if count== len(arth_list)-1:
                boo_list.append(True)
            else:
                boo_list.append(False)
        return boo_list
