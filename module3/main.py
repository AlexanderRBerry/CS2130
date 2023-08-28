import functions
import sets


def main():
    # Part 1 Sets
    print("Part 1 Sets")
    union = "∪"
    intersection = "∩"
    A = [1, 4, 3, 6, 7]
    B = [2, 3, 4, 7, 9]
    C = [1, 2, 4, 5, 6, 7, 8]

    print("Lists that represent sets A, B, and C")
    print("Set A = [1, 4, 3, 6, 7]")
    print("Set B = [2, 3, 4, 7, 9]")
    print("Set C = [1, 2, 4, 5, 6, 7, 8]")
    print("\nSet Operations")
    print("")
    print("A {} B".format(union))
    print(sets.union_of_sets(A, B))
    print("A {} B".format(intersection))
    print(sets.intersection_of_sets(A, B))
    print("A {} B {} C".format(union, union))
    print(sets.union_of_sets(sets.union_of_sets(A, B), C))
    print("A {} B {} C".format(intersection, intersection))
    print(sets.intersection_of_sets(sets.intersection_of_sets(A, B), C))
    print("(A {} B) {} C".format(union, intersection))
    print(sets.intersection_of_sets(sets.union_of_sets(A, B), C))
    print("A {} (B {} C)".format(union, intersection))
    print(sets.union_of_sets(A, sets.intersection_of_sets(B, C)))
    print("(A {} C) {} B".format(intersection, union))
    print(sets.union_of_sets(sets.intersection_of_sets(A, C), B))
    print("A {} (C {} B)".format(intersection, union))
    print(sets.intersection_of_sets(A, sets.union_of_sets(C, B)))

    # # Part 2 Functions
    # print("\nPart 2 Functions")
    #
    # print("\nFunction f")
    #
    # print("\nFunction g")
    #
    # print("\nFunction h")


if __name__ == '__main__':
    main()

