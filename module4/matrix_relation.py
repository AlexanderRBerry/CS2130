class MatrixRelation:
    def __init__(self, matrix):
        self.matrix = matrix

    def __eq__(self, other):
        if not isinstance(other, MatrixRelation):
            return False
        return self.matrix == other.matrix

    def __str__(self):
        result = '\n'.join(map(str, self.matrix))
        return result

    """
        ***********************************************************************
        * TODO:  Add your code to the methods below
        ***********************************************************************
    """
    def join(self, other):
        """ Join two matrices together by performing a
            logical OR of current matrix with matrix other
            Don't modify this matrix "in-place" (i.e. make a copy)
        """
        joinedMatrix = []
        for row in range(len(self.matrix)):
            joinedMatrix.insert(len(joinedMatrix), [])
            for column in range(len(self.matrix[row])):
                if self.matrix[row][column] or other.matrix[row][column] == 1:
                    joinedMatrix[row].insert(column, 1)
                else:
                    joinedMatrix[row].insert(column, 0)
        return MatrixRelation(joinedMatrix)

    def transpose(self):
        """ Transpose of current matrix
            Switch the rows to columns and the columns to rows
            Don't modify this matrix "in-place" (i.e. make a copy)
        """
        result = []
        for row in range(len(self.matrix[0])):
            result.insert(len(result), [])
            for column in range(len(self.matrix)):
                result[row].insert(column, self.matrix[column][row])
        return MatrixRelation(result)

    def reflexive_closure(self):
        """ Reflexive closure of current matrix
            Add the necessary arrows to make the matrix reflexive
            Don't modify this matrix "in-place" (i.e. make a copy)
        """
        # TODO: Put code here...
        return MatrixRelation(result)

    def symmetric_closure(self):
        """ Symmetric closure of current matrix
            Add the necessary arrows to make the matrix symmetric.
            You may want to consider how the transpose of the matrix
            and a join could be useful here.
            Don't modify this matrix "in-place" (i.e. make a copy)
        """
        # TODO: Put code here...
        return MatrixRelation(result)

    def in_degree(self, vertex):
        """ Number of arrows INTO node of digraph
            Nodes are numbered 0,1,2,...,SIZE-1
        """
        # TODO: Put code here...
        return 0

    def out_degree(self, vertex):
        """ Number of arrows FROM node of digraph
            Nodes are numbered 0,1,2,...,SIZE-1
        """
        # TODO: Put code here...
        return 0

    def is_rooted_tree(self):
        """ Determine if this binary relation could represent a directed rooted tree
            This means that there is exactly 1 node with in-degree of zero
            and every other node has an in-degree of 1."""
        # TODO: Put code here...
        return False
