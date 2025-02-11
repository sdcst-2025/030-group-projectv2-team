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
    
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
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
    try:
        if MILESSANDERS == 1:
            rectangle()
        elif MILESSANDERS == 2:
            rectangularprism()
        elif MILESSANDERS == 3:
            triangle()
        elif MILESSANDERS == 4:
            triangularprism()
        elif MILESSANDERS == 5:
            circle()
        elif MILESSANDERS == 6:
            sphere()
        elif MILESSANDERS == 7:
            slope()
        elif MILESSANDERS == 8:
            accumulation()
    except:
        print("invalid command")
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

def rectangle():

    milesinstructions = int(input("What Is The Width Of Your Rectangle? => "))
    jericksinstructions = int(input("What Is The Length Of Your Rectangle? => "))
    hotasthesumma = milesinstructions * jericksinstructions
    prin(f"The area is {hotasthesumma}m^2")

def rectangularprism():
    Jerick = int(input("what is the width of the rectangular prism in meters?"))
    isthe = int(input("what is the length of the rectangular prism in meters?"))
    BEST = int(input("what is the height of the rectangular prism in meters?"))
    JM1 = Jerick * isthe * BEST
    print(f"The volume is {JM1}m^3")

def triangle():

    superman = int(input("How Wide Is The Base Of Your Triangle? = >"))
    wonderwoman = int(input("What Is The Height Of Your Triangle? => "))
    hero = (superman * wonderwoman) / 2
    print(f"The Area Is {hero}m^2")

import math

def triangularprism():
    Hello = int(input("How Wide Is The Base Of Your Triangle? = >"))
    Bonjour = int(input("What Is The Height Of Your Triangle? => "))
    Hola = int(input("What Is The Length Of Your Triangular Prism? => "))
    Salut = 0.5 * Hello * Bonjour * Hola
    print(f"The Volume is {Salut}m^3")

def circle():

    readyornot = int(input("what is the radius of your circle? => "))
    coolbeans = math.pi * (readyornot ** 2)
    print(f"The area is {coolbeans}m^2")

def sphere():

def slope():

def accumulation():



if __name__ == "__main__":
    main()

