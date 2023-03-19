class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        my_stack = list()
        while j<=(len(popped)-1):
            if my_stack and my_stack[-1]==popped[j]:
                my_stack.pop()
                j+=1
            elif i<=(len(pushed))-1:
                my_stack.append(pushed[i])
                i+=1
            else:
                return False
        return len(my_stack)==0