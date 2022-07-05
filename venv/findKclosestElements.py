from typing import List
import operator
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # closestDict = {}
        # res = []
        # for i in range(len(arr)):
        #     closestDict[abs(arr[i] - x)] = closestDict.get(abs(arr[i] - x),[])
        #     closestDict[abs(arr[i] - x)].append(arr[i])
        # print(closestDict)
        # closestDict = dict(sorted(closestDict.items(), key=lambda x: x[0]))
        # print(closestDict)
        # for val in closestDict.values():
        #     res += val
        # res.sort()
        # return(res[:k])
        ans_list = []

        # for y in arr:
        #     ans_list.append((abs(y - x), y))
        #
        # print(ans_list)
        # lst = sorted(ans_list, key=operator.itemgetter(0, 1))
        #
        # # return sorted([z[1] for z in lst[:k]])
        # lst = [x[1] for x in lst[:k]]
        # lst.sort()
        # return lst

        res_list = []
        for i in arr:
            res_list.append((abs(i - x), i))
        # print(closestDict)
        res_list.sort(key=lambda x: x[0])
        # print(closestDict)
        res_list = [x[1] for x in res_list[:k]]
        res_list.sort()
        return(res_list)

    
arr = [1,2,3,4,5]
test_arr = [3,5,2,1,4]
test_arr.sort()
print("test sort = ", test_arr)
k = 4
x = 3
solution = Solution()
res = solution.findClosestElements(arr, k, x)
print(res)