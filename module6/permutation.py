
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
        #TODO: Make sure you start at the beginning (see the
        # reset_permutation method)
        #TODO: Print permutation
        #TODO: Generate a next permutation
        while True:
            print(self.current_permutation)
            if self.next_permutation() is True:
                break
        #TODO: Repeat (It helps if your next_permutation method returns a boolean)
        pass

    def next_permutation(self):

        for i in range(len(self.current_permutation) - 1, -1, -1):
            if i - 1 < 0:
                self.reset_permutation()
                return True
            nextVal = self.current_permutation[i - 1]
            if self.current_permutation[i] > nextVal:
                for j in range(len(self.current_permutation) - 1, -1, -1):
                    if self.current_permutation[j] > self.current_permutation[i - 1]:
                        self.current_permutation[i - 1] = self.current_permutation[j]
                        self.current_permutation[j] = nextVal
                        break
                self.current_permutation[i:] = sorted(self.current_permutation[i:])

                return False





        #TODO: Move from right to left until the
        # current number is less than the previous one
        #TODO: Start at the right and find the first
        # number greater than current.
        #TODO: Swap the numbers
        #TODO: Reverse the order of the numbers to the right of the swapped
        # value so that they are in increasing order.
        #TODO: When you go through the entire set and the current
        # number is never less than the previous one, reset
        # the permutation to the beginning (see reset_permutation)
        # It is helpful to return a boolean indicating if the permutation has been reset.
        pass