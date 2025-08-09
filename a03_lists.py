from collections import Counter

# List
from turtledemo.penrose import inflatedart

a = ["a",'b',1,1.1]

def print_list(element):
    print(element)

for element in a:
    print_list(element)

# List operation
list_of_month = ["January", "February", "March", "April", "May"]

# first element of list
first_month = list_of_month[0]
print(list_of_month)
list_of_month.append("June")
print(list_of_month)
# IndexError: list index out of range
# print(list_of_month[100])

array_length = len(list_of_month)
print(array_length)
for row in range(array_length):
    list_of_month.append("a")
    print(f"{row} {list_of_month[row]}")
    if row == 10:
        break

array_length = len(list_of_month)
print(array_length)
print(list_of_month)

# Q Write a function that searches for an element in an array and return the index,
# if the element is not present then just return -1

array = [1, 5, 8, 0, 2, 3]
def search_element(array, num):
    for j in range(len(array)):
        if array[j] == num:
            return j
    return -1

index_of_8 = search_element(array,8)
print(index_of_8)

# Q Write a function that return the number of negative numbers in an array
array = [-1,2,3,-9,-10,11]
def count_negative(array):
    count = 0
    for i in range(len(array)):
        if array[i] < 0:
            count += 1
    return count
print(f"Number of negative numbers in array {array} is {count_negative(array)}")

# Q Write a function that returns the largest number in an array
def count_highest_number(array):
    max_num = float('-inf')
    for i in range(len(array)):
        if array[i] > max_num:
            max_num = array[i]
    return max_num
max_num = count_highest_number(array)
print(f"max number in {array} is {max_num}")




print("default python has min max and other in array/list")
print(f"max number in {array} is {max(array)}")
print(f"min number in {array} is {min(array)}")
print(f"average number in {array} is {sum(array)/len(array)}")

# sort array in python
print(f"sorted array is {sorted(array)}")
print(f"reverse sorted array is {sorted(array, reverse=True)}")

str_array = ["a", "b", "g", "c", "d", "a", "a", "b"]
print(f"sorted str array is {sorted(str_array)}")
print(f"reverse sorted str array is {sorted(str_array, reverse=True)}")

words = ["apple", "banana", "kiwi"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['kiwi', 'apple', 'banana']

# group top 2 by count of occurrences
# Count occurrences
counts = Counter(str_array)
print(counts)
# Get the top 2 most common elements
top_2 = counts.most_common(2)
print(f"top 2 most common: {top_2}")

# two D array
a_of_array = [ [1,2],[3,4],[5,6]]
arr = []
for row in a_of_array:
    for col in row:
        arr.append(col)

print(arr)

for row in range(len(a_of_array)):
    for col in range(len(a_of_array[row])):
        arr.append(a_of_array[row][col])

print(arr)

# Q Write a function the find the second largest in the array
arr = [13,-1,10,-2,11,-3,12]
m = float("-inf")
sm = m
for i in arr:
    if m < i:
        sm = m
        m = i
    elif sm < i:
        sm = i

print(f"Second smallest element is {sm} in array {arr}")