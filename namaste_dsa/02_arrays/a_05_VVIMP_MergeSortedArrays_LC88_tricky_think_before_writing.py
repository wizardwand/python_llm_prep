from typing import List

class Solution:
    def merge1(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n ==0:
            return a
        i, j = 0, 0
        while i < m and j < n:
            if a[i] <= b[j]:
                i += 1
            elif a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
                j += 1
            print(a)
            i += 1
        j = 0
        while i < m+n and a[i] < b[j]:
            a[i] = b[j]
            i+=1
            j+=1
        print(a)

    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n ==0:
            return a
        i, j , ind = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if a[i] >= b[j]:
                a[ind] = a[i]
                i -=1
            else:
                a[ind] = b[j]
                j-=1
            ind-=1
        while i >= 0:
            a[ind] = a[i]
            i-=1
            ind-=1
        while j >= 0:
            a[ind] = b[j]
            j-=1
            ind-=1
        print(a)
        return a
# Solution().merge([1,2,3,0,0,0],3, [2,5,6], 3)
# Solution().merge([4,5,6,0,0,0],3, [1,2,3], 3)
Solution().merge([4,0,0,0,0],1, [1,2,3,5], 4)