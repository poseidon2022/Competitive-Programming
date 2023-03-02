class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        list1 = []
        list2 = []
        distance_list = []
        for i in points:
            distance = i[0]**2 + i[1]**2
            distance_list.append(distance)
        distance_list.sort()
        c = 1
        for j in distance_list:
            if c<=k:
                list1.append(j)
                c+=1
        for l in points:
            dist = l[0]**2 + l[1]**2
            if dist in list1:
                list2.append(l)
        List = list2
        return List
