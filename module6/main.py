from permutation import Permutation
from combination import Combination


def main():
    # Prompt user to input a set of positive integers (-1 to stop)
    userNums = []
    while True:
        userInput = int(input("Enter a positive integer (-1 to stop): "))
        if userInput >= 0:
            userNums.append(userInput)
        else:
            break

    # Prompt user to enter a target sum
    targetSum = int(input("Enter the target sum: "))
    # Prompt user to enter the subset length
    subsetLen = int(input("Enter the subset length: "))
    print("Subsets of length {} that sum to {}".format(subsetLen, targetSum))
    # Use the combination class to find all subsets of length n that sum to x
    userCombo = Combination(userNums, subsetLen)
    while True:
        total = 0
        for i in range(userCombo.subset_length):
            total += userCombo.current_combination[i]
        if total == targetSum:
            print(userCombo.current_combination)
        if userCombo.next_combination() is True:
            break
    # Use the permutation class to print all permutations of the set.
    print("Permutations:")
    userPerm = Permutation(userNums)
    userPerm.print_all_permutations()
    pass


# Run the main function
if __name__ == "__main__":
    main()
