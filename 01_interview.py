arr = [13,-1,10,-2,11,-3,12,13]

# remove duplicates from list
print(arr)
no_duplicate = set(arr)
print(no_duplicate)

# Print top 2 elements count in array
arr = [13,-1,10,-2,11,-3,12,13]
count_map = {}

for i in arr:
    count_map[i] = count_map.get(i, 0) + 1

print(count_map)
# sorted(count_map.values(), reverse=True)
top_2 = sorted(count_map.items(), key=lambda x: x[1], reverse=True)[:2]
print(count_map)

for num, count in top_2:
    print(f"{num} occurs {count} times in array")