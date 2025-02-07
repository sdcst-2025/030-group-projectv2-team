#!python3
# Volume Calculator
# Feel free to rename your variables


def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    print("Welcome To The Geometry/Graphing Calculator!")
    print("This Calculator Has Eight Functions")
    print("Enter \"1\" To Calculate The Area Of A Rectangle")
    print("Enter \"2\" To Calculate The Volume Of A Rectangular Prism")
    print("Enter \"3\" To Calculate The Area Of A Triangle")
    print("Enter \"4\" To Calculate The Volume Of A Triangular Prism")
    print("Enter \"5\" To Calculate The Area Of A Circle")
    print("Enter \"6\" To Calculate The Volume Of A Sphere")
    print("Enter \"7\" To Calculate The Slope Of A Graph At A Specific Point")
    print("Enter \"8\" To Calculate The Area Under A Function At An Interval")
    MILESSANDERS = input("What Would You Like To Do? => ")
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return None



def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    title()
    while True:
        # keep giving options to choose menu options until they choose to exit
        pass

if __name__ == "__main__":
    main()
