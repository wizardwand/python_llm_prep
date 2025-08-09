# how to comment
# single line comment

"""
this is
multi
line
comment
"""


# set
list = [10,20,50,20]
print(f"list is : {list}")
# remove duplicates
print(f"list with not duplicate : {set(list)}")
print(f"type : {type(set(list))}")
# map is a dict in python
map = {}
print(f"map is : {type(map)}")

month_set = {"Jan","Feb","Mar"}
# set is accessible only in loop, it's like hashset
print(f"month_set is : {month_set}")
month_set.add("April")
for month in month_set:
    print(f"month is : {month}")

month_set.remove("Jan")
# if the value not present give error
print(f"month_set is : {month_set}")
#  in list if duplicates are present , remove will remove only 1st reference
