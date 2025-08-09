
def sum_1_to_n(n:int):
    if n == 0:
        return 0
    return n + sum_1_to_n(n-1)

print(sum_1_to_n(4))