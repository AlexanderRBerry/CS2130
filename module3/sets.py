def intersection_of_sets(set1, set2):
    """
    Returns the intersection of two sets.

    :param set1: A list of integers that defines a set.
    :param set2: A list of integers that defines a set.
    :return: An ordered list of integers that represents the intersection of the two sets.
             The list is sorted from smallest to largest.
    """
    if set1 == set2:  # Nothing needs to be done if the sets are equal
        return set1
    set1.sort()
    intersectionSet = []  # This will hold the intersection of set1 and set2 with duplicates
    for i in range(len(set1)):
        for j in range(len(set2)):
            if set1[i] == set2[j]:
                intersectionSet.append(set1[i])
                break
    nonDupeIntersectionSet = remove_duplicates(intersectionSet)  # Removal of any duplicate entries
    return nonDupeIntersectionSet


def union_of_sets(set1, set2):
    """
    Returns the union of two sets.

    :param set1: A list of integers that defines a set.
    :param set2: A list of integers that defines a set.
    :return: An ordered list of integers that represents the union of the two sets.
             The list is sorted from smallest to largest.
    """
    if set1 == set2:  # Nothing needs to be done if the sets are equal
        return set1
    unionSet = set1 + set2
    unionSet.sort()
    return remove_duplicates(unionSet)


def remove_duplicates(set1):
    """
    Returns a set with all duplicates removed.

    :param set1: A list of integers that defines a set.
    :return: A list of integers with all duplicate values removed.
    """
    nonDupeSet = []
    for i in range(len(set1)):
        if set1[i] not in nonDupeSet:
            nonDupeSet.append(set1[i])
    return nonDupeSet
