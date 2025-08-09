from typing import List

class Solution:
    def moveZeroes(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """"
        i = 0
        while i < len(a):
            if a[i] == 0:
                j = i +1
                while j < len(a):
                    if a[j] == 0:
                        j +=1
                    else:
                        a[i], a[j] = a[j], a[i]
                        break
            i += 1
        """
        i , x = 0, 0
        while i < len(a):
            if a[i] != 0:
                a[x] = a[i]
                x += 1
            i +=1

        while x < len(a):
            a[x] = 0
            x += 1
        print(a)

Solution().moveZeroes([0,1,0,3,12])