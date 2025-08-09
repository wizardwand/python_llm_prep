from typing import List

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # return s.reverse()
    left , right = 0 , len(s)-1
    while left < right:
        s[left], s[right] = s[right],s[left]
        left +=1
        right -= 1

input_list = list("abc")
reverseString(input_list)
print(input_list)
