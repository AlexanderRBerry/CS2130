from matrix_relation import MatrixRelation

def main():
    # Create the MatrixRelation that represents
    # the image in the instructions
    # Print the MatrixRelation
    # Print the reflexive closure of the relation
    # Print the symmetric closure of the relation
    # Print a statement indicating if the relation
    # is a rooted tree or not

    myMatrix = MatrixRelation([
        [1, 1, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 1]
    ])

    print(len(myMatrix.matrix))
    print(len(myMatrix.matrix[0]))
    print(myMatrix)
    print()
    print(MatrixRelation.symmetric_closure(myMatrix))
    return

if __name__ == '__main__':
    main()
