"""
print()         -> prints the output console
input()         -> get data from console
set()           -> takes a list , removes duplicate and gives set
int()           -> takes string and converts to int

# on the value
"2, 3".split()
# each data type has on the value functions
"""

"text".split()
count = [1, 3, 5, 1].count(1)
print(count)
list = ["a","b","c","d","a"]
a_count = list.count("a")
print(a_count)
alphabet_count = {}
for item in list:
    if item not in alphabet_count:
        alphabet_count[item] = list.count(item)

print(alphabet_count) # {'a': 2, 'b': 1, 'c': 1, 'd': 1}
alphabet_count = sorted(alphabet_count.items(), key=lambda x: x[1], reverse=True)[:3]
print(alphabet_count) # [('a', 2), ('b', 1), ('c', 1)]


from collections import Counter

top3 = Counter(list).most_common(3)
print(top3)

Counter(list)


"""
Python Collection
from collections import Counter

top3 = Counter(my_list).most_common(3)
print(top3)

Java Streams and collection 

LinkedHashMap<String, Long> result = list.stream()
    .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
    .entrySet().stream()
    .sorted(Map.Entry.<String, Long>comparingByValue().reversed())
    .limit(3) // get Top 3
    // .skip(3) // get 4th and rest
    .collect(Collectors.toMap(
        Map.Entry::getKey,
        Map.Entry::getValue,
        (e1, e2) -> e1,
        LinkedHashMap::new
    ));
"""