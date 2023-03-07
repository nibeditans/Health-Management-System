# Health Management System
# There are 3 clients - Chicku, Picku and Jani

def getdate():
    import datetime
    return datetime.datetime.now()


# Total 6 files
# Write a function that takes as input client name when executed
# One more function to retrieve exercise or food for any client


# Here is the Code Dude
import datetime

def gettime():
    return datetime.datetime.now()

def take(n):
    if n == 1:
        j = int(input("Enter 1 for excersise & 2 for food: "))
        if j == 1:
            value = input("Type here\n")
            with open("Chicku-ex.txt", "a") as cp:
                cp.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
        elif j == 2:
            value = input("Type here\n")
            with open("Chicku-food.txt", "a") as cp:
                cp.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    elif n == 2:
        j = int(input("Enter 1 for excersise & 2 for food: "))
        if j == 1:
            value = input("Type here\n")
            with open("Picku-ex.txt", "a") as cp:
                cp.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
        elif j == 2:
            value = input("Type here\n")
            with open("Picku-food.txt", "a") as cp:
                cp.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    elif n == 3:
        j = int(input("Enter 1 for excersise & 2 for food: "))
        if j == 1:
            value = input("Type here\n")
            with open("Jani-ex.txt", "a") as cp:
                cp.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
        elif j == 2:
            value = input("Type here\n")
            with open("Jani-food.txt", "a") as cp:
                cp.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    else:
        print("Please enter valid input (1(Chicku),2(Picku),3(Jani)")

def retrieve(n):
    if n == 1:
        j = int(input("Enter 1 for excersise & 2 for food: "))
        if j == 1:
            with open("Chicku-ex.txt") as cp:
                for i in cp:
                    print(i, end="")
        elif j == 2:
            with open("Chicku-food.txt") as cp:
                for i in cp:
                    print(i, end="")
    elif n == 2:
        j = int(input("Enter 1 for excersise & 2 for food: "))
        if j == 1:
            with open("Picku-ex.txt") as cp:
                for i in cp:
                    print(i, end="")
        elif j == 2:
            with open("Picku-food.txt") as cp:
                for i in cp:
                    print(i, end="")
    elif n == 3:
        j = int(input("Enter 1 for excersise & 2 for food: "))
        if j == 1:
            with open("Jani-ex.txt") as cp:
                for i in cp:
                    print(i, end="")
        elif j == 2:
            with open("Jani-food.txt") as cp:
                for i in cp:
                    print(i, end="")
    else:
        print("Please enter valid input (Chicku, Picku and Jani)")


print("Health Management System! ")
a = int(input("Press 1 for log the value & 2 for retrieve the value: "))

if a == 1:
    b = int(input("Press 1 for Chicku, 2 for Picku & 3 for Jani: "))
    take(b)
else:
    b = int(input("Press 1 for Chicku, 2 for Picku & 3 for Jani: "))
    retrieve(b)
