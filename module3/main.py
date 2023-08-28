import functions
import sets


def main():
    # Part 1 Sets
    print("Part 1 Sets")
    A = [1, 4, 3, 6, 7, 7, 7, 7]

    B = [2, 3, 4, 7, 9]

    C = [1, 2, 4, 5, 6, 7, 8, 7, 7, 7, 7]

    D = sets.intersection_of_sets(A, C)
    E = sets.union_of_sets(A, B)
    print(D)
    print(E)
    # print("Lists that represent sets A, B, and C")
    #
    # print("\nSet Operations")
    #
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

