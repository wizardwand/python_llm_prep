from typing import List

def removeElement(nums: List[int], val: int) -> int:
    print(nums)
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1

    del nums[j:]
    print(nums)

# nums = [3,2,2,3]
nums = [0,1,2,2,3,0,4,2]
val = 2
removeElement(nums, val)