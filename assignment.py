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
    print("Enter \"7\" To Calculate The Volume Of A Cone")
    print("Enter \"8\" To Calculate The Slope Of A Graph At A Specific Range")
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
            cone()
        elif MILESSANDERS == 8:
            slope()
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
    print(f"The Area Is {hotasthesumma}m^2")

def rectangularprism():
    Jerick = int(input("What Is The Width Of The Rectangular Prism In Meters?"))
    isthe = int(input("What Is The Length Of The Rectangular Prism In Meters?"))
    BEST = int(input("What Is The Height Of The Rectangular Prism In Meters?"))
    JM1 = Jerick * isthe * BEST
    print(f"The Volume Is {JM1}m^3")

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
    print(f"The Volume Is {Salut}m^3")

def circle():
    readyornot = int(input("What Is The Radius Of Your Circle? => "))
    coolbeans = math.pi * (readyornot ** 2)
    print(f"The Area Is {coolbeans}m^2")

def sphere():
    How = int(input("What Is The Radius Of Your Sphere? => "))
    Are = (4/3)*math.pi*How**3
    You = round(Are,2)
    print(f"The Volume Of Your Sphere Is {You}m^3")

def cone():
    Creep = int(input("What Is The Radius Of Your Base? => "))
    NoSurprises = int(input("What Is The Height Of Your Cone? => "))
    KarmaPolice = math.pi*Creep**2*(NoSurprises/3)
    Radio = round(KarmaPolice,2)
    print(f"The Volume of your cone is {Radio}m^3")

def slope():
    delf0 = int(input("What Is The Y-value At Your First Point"))
    delf1 = int(input("what Is The X-value At Your First Point"))
    delf2 = int(input("what Is The Y-value At Your Second Point"))
    delf3 = int(input("what Is The X-value At Your Second Point"))
    delfexam = (delf2 - delf0) / (delf3 - delf1)
    print(f"The Slope Is {delfexam}m/s")

if __name__ == "__main__":
    main()

