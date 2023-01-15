class Solution:
    def sortSentence(self, s: str) -> str:
        list1 = [""]
        final = ""
        for i in s:
            if i==" ":
                list1.append("")
        temp = ""
        for i in s:
            if i.isnumeric()==True:
                list1[int(i)-1] = temp
                temp = ""
            elif i!=" ":
                temp+=i
        for i in range(0,len(list1)):
            if i==0:
                final+=list1[i]
            else:
                final = final+" "+list1[i]
        return final
