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
    print("\nPart 2 Functions")

    print("\nFunction f")
    print("Domain = {4, 6, 7, 9, 12}")
    print("Target = {3, 5, 7, 9, 15}")
    print("Range = {7, 9, 3, 15, 5}")
    print("f:X -> Y")
    print("f:{(4, 7), (6, 9), (7, 3), (9, 15), (12, 5)}")
    X = [4, 6, 7, 9, 12]
    Y = [3, 5, 7, 9, 15]
    R = [7, 9, 3, 15, 5]
    print("Injective: {}".format(functions.is_one_to_one(X, Y, R)))
    print("Surjective: {}".format(functions.is_onto(X, Y, R)))
    print("Bijective: {}".format(functions.is_bijection(X, Y, R)))

    print("\nFunction g")
    print("Domain = {3, 8, 11, 13, 22}")
    print("Target = {8, 11, 16, 18}")
    print("Range = {18, 16, 11, 8, 11}")
    print("f:X -> Y")
    print("f:{(3, 18), (8, 16), (11, 11), (13, 8), (22, 11)}")
    X = [3, 8, 11, 13, 22]
    Y = [8, 11, 16, 18]
    R = [18, 16, 11, 8, 11]
    print("Injective: {}".format(functions.is_one_to_one(X, Y, R)))
    print("Surjective: {}".format(functions.is_onto(X, Y, R)))
    print("Bijective: {}".format(functions.is_bijection(X, Y, R)))

    print("\nFunction h")
    print("Domain = {2, 4, 5, 6, 9}")
    print("Target = {1, 4, 7, 8, 11, 13}")
    print("Range = {4, 7, 1, 6, 8, 11}")
    print("f:X -> Y")
    print("f:{(2, 4), (4, 7), (5, 1), (6, 8), (9, 11)}")
    X = [2, 4, 5, 6, 9]
    Y = [1, 4, 7, 8, 11, 13]
    R = [4, 7, 1, 6, 8, 11]
    print("Injective: {}".format(functions.is_one_to_one(X, Y, R)))
    print("Surjective: {}".format(functions.is_onto(X, Y, R)))
    print("Bijective: {}".format(functions.is_bijection(X, Y, R)))


if __name__ == '__main__':
    main()

