
class Permutation:
    def __init__(self, values):
        set_values = sorted(set(values))
        self.current_permutation = list(set_values)

    def reset_permutation(self):
        self.current_permutation.sort()

    def get_permutation(self):
        return list(self.current_permutation)

    def set_permutation(self, perm):
        set_perm = sorted(set(perm))
        if len(set_perm) != len(self.current_permutation) and len(set_perm) != len(perm):
            return
        for value in set_perm:
            if value not in self.current_permutation:
                return
        self.current_permutation = list(perm)

    def print_all_permutations(self):
        self.reset_permutation()


        while True:
            # Print permutations
            print(self.current_permutation)
            # Generate a next permutation
            if self.next_permutation() is True:
                break
        pass

    def next_permutation(self):
        # Move from right to left until the current number is less than the previous one
        for i in range(len(self.current_permutation) - 1, -1, -1):
            # Don't go out of bounds, this means you are at the end
            if i - 1 < 0:
                self.reset_permutation()
                return True
            nextVal = self.current_permutation[i - 1]
            if self.current_permutation[i] > nextVal:
                for j in range(len(self.current_permutation) - 1, -1, -1):
                    # Start at the right and find the first
                    # number greater than current.
                    if self.current_permutation[j] > self.current_permutation[i - 1]:
                        # Swap the numbers
                        self.current_permutation[i - 1] = self.current_permutation[j]
                        self.current_permutation[j] = nextVal
                        break
                # Reverse the order of the numbers to the right of the swapped
                # value so that they are in increasing order.
                self.current_permutation[i:] = sorted(self.current_permutation[i:])

                return False
        pass
