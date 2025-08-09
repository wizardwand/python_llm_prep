
# with reversing the string
def is_palindrome(s):
    rev = s[::-1]
    return rev == s

print(f"aba: {is_palindrome('aba')}")
print(f"abc: {is_palindrome('abc')}")
print(f"racecar: {is_palindrome('racecar')}")

# in place comprising
def is_palindrome_inplace(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

print(f"aba: {is_palindrome_inplace('aba')}")
print(f"abc: {is_palindrome_inplace('abc')}")
print(f"raceCAR: {is_palindrome_inplace('raceCAR')}")

#  # Skip non-alphanumeric characters
#         while left < right and not s[left].isalnum():
#             left += 1
#         while left < right and not s[right].isalnum():
#             right -= 1