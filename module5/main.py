from functions import *


def main():
    # Part 1, run geometric sequence
    print("\nGeometric Sequences")
    print("\n7 terms starting with 5.63 and a common ratio of 3.2")
    print(geometric_sequence(7, 5.63, 3.2))
    print("\n9 terms starting with 3.78 and a common ratio of 7.124")
    print(geometric_sequence(9, 3.78, 7.124))
    print("\n6 terms starting with 8 and a common ratio of 3")
    print(geometric_sequence(6, 8, 3))
    # Part 1, run arithmetic sequence
    print("\nArithmetic Sequences")
    print("\n7 terms starting with 5.63 and a common difference of 3.2")
    print(arithmetic_sequence(7, 5.63, 3.2))
    print("\n9 terms starting with 3.78 and a common difference of 7.124")
    print(arithmetic_sequence(9, 3.78, 7.124))
    print("\n6 terms starting with 8 and a common difference of 3")
    print(arithmetic_sequence(6, 8, 3))
    # Part 2, run div and mod
    print("\nUsing Div and Mod")
    print("43 / 8")
    print(div_mod(43, 8))
    print("\n-43 / 8")
    print(div_mod(-43, 8))
    print("\n371 / 22")
    print(div_mod(371, 22))
    print("\n-371 / 22")
    print(div_mod(-371, 22))
    # Part 2, run gcd and lcm
    print("\nUsing Gcd and Lcm")
    print("72 and 124:")
    print(gcd(72, 124))
    print(lcm(72, 124))
    print("\n84 and 36:")
    print(gcd(84, 36))
    print(lcm(84, 36))
    print("\n93 and 75:")
    print(gcd(93, 75))
    print(lcm(93, 75))
    print("\n18624 and 21088:")
    print(gcd(18624, 21088))
    print(lcm(18624, 21088))

if __name__ == '__main__':
    main()
