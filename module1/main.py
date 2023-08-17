# A simple Python code to print truth tables for propositions and boolean
# expressions

# Import the Logic and Boolean modules
import logic
import boolean


def main():
    # Print truth table for proposition 1
    print("  p | q | r | proposition 1")

    print("  T | T | T | ", logic.proposition1('T', 'T', 'T'))
    print("  T | T | F | ", logic.proposition1('T', 'T', 'F'))
    print("  T | F | T | ", logic.proposition1('T', 'F', 'T'))
    print("  T | F | F | ", logic.proposition1('T', 'F', 'F'))
    print("  F | T | T | ", logic.proposition1('F', 'T', 'T'))
    print("  F | T | F | ", logic.proposition1('F', 'T', 'F'))
    print("  F | F | T | ", logic.proposition1('F', 'F', 'T'))
    print("  F | F | F | ", logic.proposition1('F', 'F', 'F'))
    print("")



    # Print truth table for proposition 2
    print("  p | q | r | proposition 2")

    print("  T | T | T | ", logic.proposition2('T', 'T', 'T'))
    print("  T | T | F | ", logic.proposition2('T', 'T', 'F'))
    print("  T | F | T | ", logic.proposition2('T', 'F', 'T'))
    print("  T | F | F | ", logic.proposition2('T', 'F', 'F'))
    print("  F | T | T | ", logic.proposition2('F', 'T', 'T'))
    print("  F | T | F | ", logic.proposition2('F', 'T', 'F'))
    print("  F | F | T | ", logic.proposition2('F', 'F', 'T'))
    print("  F | F | F | ", logic.proposition2('F', 'F', 'F'))
    print("")


    # Print truth table for proposition 3
    print("  p | q | r | proposition 3")

    print("  T | T | T | ", logic.proposition3('T', 'T', 'T'))
    print("  T | T | F | ", logic.proposition3('T', 'T', 'F'))
    print("  T | F | T | ", logic.proposition3('T', 'F', 'T'))
    print("  T | F | F | ", logic.proposition3('T', 'F', 'F'))
    print("  F | T | T | ", logic.proposition3('F', 'T', 'T'))
    print("  F | T | F | ", logic.proposition3('F', 'T', 'F'))
    print("  F | F | T | ", logic.proposition3('F', 'F', 'T'))
    print("  F | F | F | ", logic.proposition3('F', 'F', 'F'))
    print("")


    # Print truth table for Boolean expression 1
    print("  x | y | z | expression 1")

    print("  0 | 0 | 0 | ", boolean.expression1(0, 0, 0))
    print("  0 | 0 | 1 | ", boolean.expression1(0, 0, 1))
    print("  0 | 1 | 0 | ", boolean.expression1(0, 1, 0))
    print("  0 | 1 | 1 | ", boolean.expression1(0, 1, 1))
    print("  1 | 0 | 0 | ", boolean.expression1(1, 0, 0))
    print("  1 | 0 | 1 | ", boolean.expression1(1, 0, 1))
    print("  1 | 1 | 0 | ", boolean.expression1(1, 1, 0))
    print("  1 | 1 | 1 | ", boolean.expression1(1, 1, 1))


    # Print truth table for Boolean expression 2
    print("  x | y | z | expression 2")

    print("  0 | 0 | 0 | ", boolean.expression2(0, 0, 0))
    print("  0 | 0 | 1 | ", boolean.expression2(0, 0, 1))
    print("  0 | 1 | 0 | ", boolean.expression2(0, 1, 0))
    print("  0 | 1 | 1 | ", boolean.expression2(0, 1, 1))
    print("  1 | 0 | 0 | ", boolean.expression2(1, 0, 0))
    print("  1 | 0 | 1 | ", boolean.expression2(1, 0, 1))
    print("  1 | 1 | 0 | ", boolean.expression2(1, 1, 0))
    print("  1 | 1 | 1 | ", boolean.expression2(1, 1, 1))


    # Print truth table for Boolean expression 3
    print("  x | y | z | expression 3")

    print("  0 | 0 | 0 | ", boolean.expression3(0, 0, 0))
    print("  0 | 0 | 1 | ", boolean.expression3(0, 0, 1))
    print("  0 | 1 | 0 | ", boolean.expression3(0, 1, 0))
    print("  0 | 1 | 1 | ", boolean.expression3(0, 1, 1))
    print("  1 | 0 | 0 | ", boolean.expression3(1, 0, 0))
    print("  1 | 0 | 1 | ", boolean.expression3(1, 0, 1))
    print("  1 | 1 | 0 | ", boolean.expression3(1, 1, 0))
    print("  1 | 1 | 1 | ", boolean.expression3(1, 1, 1))


if __name__ == '__main__':
    main()
