import utilities


def main():
    #Prompt the user to enter their name
    #Use the utilities.hello function to say hello to the user
    name = input("Enter your name:")
    utilities.hello(name)
    return

if __name__ == '__main__':
    main()