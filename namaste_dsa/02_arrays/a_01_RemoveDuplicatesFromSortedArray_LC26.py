from typing import List

arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

def myDef(arr):
    # remove duplicates from sorted
    j = 0
    for i in range(0, len(arr)):
        if arr[i] > arr[j]:
            arr[j + 1] = arr[i]
            j = j + 1

    print(arr)
    for j in range(j + 1, len(arr)):
        arr[j] = 0

    print(arr)


def removeDuplicates(a: List[int]) -> int:
    # remove duplicates from sorted
    j = 0
    for i in range(0, len(a)):
        if a[i] > a[j]:
            a[j + 1] = a[i]
            j = j + 1

    # print(a)
    # a1 = a
    # a = []
    # for j in range(0,j):
    #     a.add(a1[j])
    del a[j + 1:]
    print(a)

removeDuplicates(arr)
