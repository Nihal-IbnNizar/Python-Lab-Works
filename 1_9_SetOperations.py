def set_operations(set1, set2):

    set_union = set1.union(set2)
    set_intersection = set1.intersection(set2)
    set_difference = set1.difference(set2)
    #set_difference = set2.difference(set1)
    
    return set_union, set_intersection, set_difference

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set_union, set_intersection, set_difference = set_operations(set1, set2)

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set_union}")
print(f"Intersection: {set_intersection}")
print(f"Difference (Set 1 - Set 2): {set_difference}")
#print(f"Difference (Set 2 - Set 1): {set_difference}")
