class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        my_stack = list()
        num_stack = list()
        index = -1
        for i in temperatures:
            num_stack.append(0)
        for i in range(len(temperatures)):
            while my_stack and my_stack[-1][0]<temperatures[i]:
                num_stack[my_stack[-1][1]] = i - my_stack[-1][1] 
                my_stack.pop()
            my_stack.append((temperatures[i],i))
        return num_stack