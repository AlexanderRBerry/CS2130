import collections


class Combination:
    def __init__(self, values, subset_len):
        set_values = sorted(set(values))
        self.combination_set = list(set_values)
        self.subset_length = subset_len
        self.current_combination = list(self.combination_set[:subset_len])

    def reset_combination(self):
        self.current_combination = list(self.combination_set[:self.subset_length])

    def get_combination(self):
        return list(self.current_combination)

    def set_combination(self, combo):
        set_combo = sorted(set(combo))
        if len(set_combo) != self.subset_length:
            return
        for value in set_combo:
            if value not in self.combination_set:
                return
        self.current_combination = list(combo)

    def print_all_combinations(self):

        self.reset_combination()
        # Print combinations
        while True:
            print(self.current_combination)
            # Generate a next Combination
            if self.next_combination() is True:
                break
        pass

    def next_combination(self):
        # Move from right to left in both the currentCombination and the combinationSet
        sizeDiff = len(self.combination_set) - self.subset_length
        for i in range(len(self.current_combination) - 1, -1, -1):
            if self.current_combination[i] != self.combination_set[i + sizeDiff]:
                # Find startPos as 1 plus the position of the number from the current combination that did
                # not match in the combinationSet.
                index = self.combination_set.index(self.current_combination[i]) + 1
                # Fill in from left to right in the currentCombination starting at the position of the mismatch
                self.current_combination[i:] = self.combination_set[index:(self.subset_length - i + index)]
                return False
        self.reset_combination()
        return True
        pass
