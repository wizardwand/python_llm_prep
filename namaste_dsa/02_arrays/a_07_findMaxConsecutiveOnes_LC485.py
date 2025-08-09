from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, a: List[int]) -> int:
        i , cur , mc1 = 0, 0, 0
        while i < len(a):
            if a[i] == 1:
                cur += 1
                if cur > mc1:
                    mc1 = cur
            else:
                cur = 0
            i += 1
        print(mc1)
        return mc1

Solution().findMaxConsecutiveOnes([1,1,0,1,1,1])
Solution().findMaxConsecutiveOnes([1,0,1,1,0,1])