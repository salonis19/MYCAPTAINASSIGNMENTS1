# adding more element to a set
my_first_set = {1,2,3,'a'}
my_first_set.add('b')
print(my_first_set)

# union of two sets
set_one = {1,2,3,4}
set_two = {'One','Two','Three','Four'}
union_of_two_sets = set_one.union(set_two)
print(union_of_two_sets)

# the intersection of two sets
set_one = {1,2,3,4, 'Five', 5}
set_two = {'One','Two','Three','Four','Five', 5}
intersection_of_two_sets = set_one.intersection(set_two)
print(intersection_of_two_sets)

# find the difference between two sets
set_one = {1,2,3,4, 'Five', 5}
set_two = {'One','Two','Three','Four','Five', 5}
difference_of_two_sets = set_one.difference(set_two)
print(difference_of_two_sets)

# deleting elements from a set
my_first_set = {1, 3, 5, 6, 0, 9}
print(my_first_set)
my_first_set.discard(9)
print(my_first_set)
