# /usr/bin/env python3
'''

@author: Sam Fenton
@Date_Finsihed: 26.04.2014

'''

import time, os


def main():
    print("")
    print("E-Recipe Book V 6.0")
    print("")
    print("Choose 1 for Flapjack")
    print("Choose 2 for Shortbread")
    print("Choose 3 to add your own recipe")
    print("Choose 4 to remove your custom recipe")
    print("Choose 5 to view your custom recipe")

    recipeChoice = input("Enter Choice: ")

    if recipeChoice == "1":
        os.system("clear")
        flapJack = open("Flapjack.txt", "r")
        
        for line in flapJack:
            print((line.rstrip()))

        flapJack.close()

        close = eval(input("Type 1 to close or 2 to stay open: "))

        if close == 1:
            print("You have chosen close...  You will be promted if you want to use this book again")
            time.sleep(2)
            redo()

        elif close == 2:
            print("The Recipe will remain open for 30 Seconds.")
            time.sleep(30)
            os.system("clear")
            redo()

        else:
            print("You Aren't a good cook as this isn't a valid option!")
            time.sleep(1)
            os.system("clear")
            main()

                
        
    elif recipeChoice == "2":
        os.system("clear")
        shortBread = open("Short Bread.txt", "r")

        for line in shortBread:
            print((line.rstrip()))

        shortBread.close()

        close = eval(input("Type 1 to close or 2 to stay open: "))

        if close == 1:
            print("You have chosen close...")
            time.sleep(2)
            redo()

        elif close == 2:
            print("The Recipe will remain open for 30 Seconds, after which you will be prompted if you want to use this book again.")
            time.sleep(30)
            os.system("clear")
            redo()

        else:
            print("You Aren't a good cook as this isn't a valid option!")
            time.sleep(1)
            os.system("clear")
            main()
                
    elif recipeChoice == "3":
        print("You have chosen add your own recipe, re-directing...")
        time.sleep(1)
        os.system("clear")
        add()

    elif recipeChoice == "4":
        print("You have chosen to remove the existing homemade recipe...")
        time.sleep(1)
        os.system("clear")
        remove()

    elif recipeChoice == "5":
        print("You have chosen to view your own custom recipe, re-directing...")
        time.sleep(1)
        os.system("clear")
        edit()

    elif recipeChoice == "":
        main()


    else:
        print("You Aren't a good cook as this isn't a valid option!")
        time.sleep(1)
        os.system("clear")
        main()


def redo():
    again = eval(input("Choose 1 if you want to use the book again, choose 2 if you don't: "))

    if again == 1:
        print("You will be re-directed to the start...")
        time.sleep(1)
        os.system("clear")
        main()

    elif again == 2:
        print("Closing Program...")
        time.sleep(1)
        exit()

    else:
        print("You Aren't a good cook as this isn't a valid option!")
        time.sleep(1)
        os.system("clear")
        main()



def add():

    os.system("clear")

    titlew = input("Title your recipe (WARNING: Will overwrite current recipe): ")

    titley = "Title: %s" % titlew
    
    if titlew == "":
        titley = "Title: [NONAME]"

    title = open("name.txt", "w")

    title.writelines(titley)

    title.close()

    template = open("template1.txt", "w")

    ing = input("Input name of Ingrediant 1: ")
    ing2 = input("Input name of Ingrediant 2: ")
    ing3 = input("Input name of Ingrediant 3: ")
    ing4 = input("Input name of Ingrediant 4: ")
    ing5 = input("Input name of Ingrediant 5: ")
    meth = input("Input Methord: ")


    ingg = ["Ingrediants: " + ing + ", ", ing2 + ", ", ing3 + ", ", ing4 + " " + "and ", ing5 + "."]
    metho = " Methord: " + meth

    template.writelines(ingg)
    template.writelines(metho)

    template.close()

    template = open("template1.txt", "r")

    list = template.readlines()

    template.close()

    cook()


def remove():

    os.system("clear")

    list = ""

    template = open("template1.txt", "w")
    template = open("template1.txt", "r")

    time.sleep(1)

    print("Opening template1.txt...")

    time.sleep(1)

    print("Overwriting template1.txt...")

    for line in template:
        template.writelines(list)

    template.close()
    template.close()

    quantites = open("quantites.txt", "w")
    quantites = open("quantites.txt", "r")

    time.sleep(1)

    print("Opening quantites.txt...")

    time.sleep(1)
    
    print("Overwriting quantites.txt...")

    for int in quantites:
        quantites.writelines(list)

    quantites.close()
    quantites.close()

    title = open("name.txt", "w")
    title = open("name.txt", "r")

    time.sleep(1)

    print("Opening name.txt...")

    time.sleep(1)

    print("Overwiting name.txt...")

    for line in title:
        title.writelines(list)

    title.close()
    title.close()

    print("Finished!")

    time.sleep(1)

    redo()





def cook():

    quantites = open("quantites.txt", "w")

    list = []
    
    qu = eval(input("Input quantites (not units) of ingrediant 1: "))
    unit1 = input("Input unit (not quantites) of Ingrediant 1: ")
    qu2 = eval(input("Input quantites (not units) of ingrediant 2: "))
    unit2 = input("Input unit of (not quantites) Ingrediant 2: ")
    qu3 = eval(input("Input quantites (not units) of ingrediant 3: "))
    unit3 = input("Input unit (not quantites) of Ingrediant 3: ")
    qu4 = eval(input("Input quantites (not units) of ingrediant 4: "))
    unit4 = input("Input unit (not quantites) of Ingrediant 4: ")
    qu5 = eval(input("Input quantites (not units) of ingrediant 5: "))
    unit5 = input("Input unit (not quantites) of Ingrediant 5: ")
    amo = eval(input("Input amount of people: "))



    total = ["Quantites --> " + str(qu*amo) + unit1 + ", ", str(qu2*amo) + unit2 + ", ", str(qu3*amo) + unit3 + ", ", str(qu4*amo) + unit4 + ", ", str(qu5*amo) + unit5 + "."]


    quantites.writelines(total)


    quantites.close()

    title = open("name.txt", "r")

    list = title.readlines()

    for line in list:
        print((line.rstrip()))

    title.close()


    template = open("template1.txt", "r+")

    os.system("clear")

    for line in template:
        print((line.rstrip()))


    list = template.readlines()

    template.close()

    quantites = open("quantites.txt", "r")

    for line in quantites:
        print((line.rstrip()))

    list = quantites.readlines()

    quantites.close()

    redo()


def edit():
    os.system("clear")

    list = []

    title = open("name.txt", "r")

    list = title.readlines()


    for line in list:
        print((line.rstrip()))

    title.close()


    template = open("template1.txt", "r")

    list = template.readlines()

    for line in list:
        print((line.rstrip()))


    linex = "No Recipe Detected"
    lineb = "Option Unavailable, Re-Directing to the start..."


    template.close()


    quantites = open("quantites.txt", "r")

    text = ""

    text = quantites.readlines()

    for line in text:
        print((line.rstrip()))


    if text == "":
        os.system("clear")
        print(linex)
        print(lineb)
        answer = ""
        time.sleep(1)
        os.system("clear")
        main()

    answer = eval(input("Enter Choice (1 to edit) (2 to leave as it is): "))

    quantites.close()

    if answer == 1:

        list = ""

        qu = eval(input("Input quantites (not units) of ingrediant 1: "))
        unit1 = input("Input unit (not quantites) of Ingrediant 1: ")
        qu2 = eval(input("Input quantites (not units) of ingrediant 2: "))
        unit2 = input("Input unit of (not quantites) Ingrediant 2: ")
        qu3 = eval(input("Input quantites (not units) of ingrediant 3: "))
        unit3 = input("Input unit (not quantites) of Ingrediant 3: ")
        qu4 = eval(input("Input quantites (not units) of ingrediant 4: "))
        unit4 = input("Input unit (not quantites) of Ingrediant 4: ")
        qu5 = eval(input("Input quantites (not units) of ingrediant 5: "))
        unit5 = input("Input unit (not quantites) of Ingrediant 5: ")
        amo = eval(input("Input amount of people: "))
        

        quantites = open("quantites.txt", "w")


        total = ["Quantites --> " + str(qu*amo) + unit1 + ", ", str(qu2*amo) + unit2 + ", ", str(qu3*amo) + unit3 + ", ", str(qu4*amo) + unit4 + ", ", str(qu5*amo) + unit5 + "."]

        quantites.writelines(total)

        quantites.close()

        template = open("template1.txt", "r+")

        os.system("clear")

        title = open("name.txt", "r")

        list = title.readlines()

        for line in list:
            print((line.rstrip()))

        title.close()

        template = open("template1.txt", "r")

        list = template.readlines()

        for line in list:
            print((line.rstrip()))

        template.close()

        quantites = open("quantites.txt", "r")

        list = quantites.readlines()

        for line in list:
            print((line.rstrip()))


        quantites.close()

        redo()

    elif answer == 2:
        print("No changes will be made...")
        time.sleep(1)
        redo()

    else:
        print("You Aren't a good cook as this isn't a valid option!")
        time.sleep(1)
        os.system("clear")
        main()

if __name__ == '__main__':
    main()

