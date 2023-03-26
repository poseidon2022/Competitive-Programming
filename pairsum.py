class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        my_list = list()
        while head:
            my_list.append(head.val)
            head = head.next
        i = 0
        j = len(my_list)-1
        maxim = 0
        while i<j:
            sum = my_list[i]+my_list[j]
            if sum>maxim:
                maxim = sum
            i+=1
            j-=1
        return maxim