
a = [1, 5]
# using array sum function
def sum_arr():
    return sum(a)

def sum_arr_manually(n):
    if n == len(a):
        return 0
    else:
        return a[n] + sum_arr_manually(n+1)
print(sum_arr())
print(sum_arr_manually(0))