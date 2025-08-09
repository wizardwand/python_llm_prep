class Solution:
    rm = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    @staticmethod
    def roman_to_int(s: str) -> int:
    # def roman_to_int(s):
        rm = Solution.rm
        left = 0
        total = 0
        while left < len(s):
            ch = s[left]
            n = left + 1
            if n < len(s) and rm[ch] < rm[s[n]]:
                total += (rm[s[n]] -rm[ch])
                left += 2
            else:
                total += rm[ch]
                left += 1
        return total


sol = Solution()
print(f"MCMXCIV -> {sol.roman_to_int('MCMXCIV')}")
print(f"III -> {Solution.roman_to_int('III')}")
print(f"LVIII -> {Solution.roman_to_int('LVIII')}")