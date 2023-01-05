def insertionSort1(n, arr):
    # Write your code here
    num = arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>num:
            if arr[i]>num and num==1 and i==0:
                arr[1] = arr[0]
                for i in arr:
                    print(i,end=" ")
                print()
                arr[0] = 1
                for j in arr:
                    print(j,end=" ")
                break
            else:
                arr[i+1] = arr[i]
                for j in arr:
                    print(j,end=" ")
            print()
        elif arr[i]<num:
            arr[i+1] = num
            for j in arr:
                print(j,end=" ")
            break