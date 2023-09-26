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
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 0],
    ])
    print("myMatrix")
    print(myMatrix)
    print()
    print("Reflexive closure of myMatrix \n{}\n".format(MatrixRelation.reflexive_closure(myMatrix)))
    print("Symmetric closure of myMatrix \n{}\n".format(MatrixRelation.symmetric_closure(myMatrix)))
    print("This graph could be represented as a rooted tree: {}".format(MatrixRelation.is_rooted_tree(myMatrix)))

    return

if __name__ == '__main__':
    main()
