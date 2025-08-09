
# print 1 to n recursively

def print1_to_n(n:int):
    if n == 0:
        return
    print1_to_n(n-1)
    print(n)

print1_to_n(3)

def print_n_to_1(n:int):
    if n == 0:
        return
    print(n)
    print_n_to_1(n-1)

print_n_to_1(3)