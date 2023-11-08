from permutation import Permutation
from combination import Combination


def main():
    #TODO: Prompt user to input a set of positive integers (-1 to stop)
    #myList = list(input("Please enter a list of numbers -1 to stop"))
    #TODO: Prompt user to enter a target sum
    #TODO: Prompt user to enter the subset length
    #TODO: Use the combination class to find all subsets of length n that sum to x
    #TODO: Use the permutation class to print all permutations of the set.
    myPerm = Permutation((2, 1, 3))
    myPerm.print_all_permutations()
    pass


# Run the main function
if __name__ == "__main__":
    main()
