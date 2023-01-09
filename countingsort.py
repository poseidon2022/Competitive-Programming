def countingSort(arr):
        list1 = []
        for i in range(100):
            list1.append(0)
        for i in arr:
            list1[i]+=1
        return list1