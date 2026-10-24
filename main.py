import opt1_main
import opt2_main
import opt3_main
import opt4_main
import opt5_main
import opt6_main

# remove by criteria iti trebuie un search sau ceva (daca e lista gigantica ce faci)


concerts = {}


def opt1():
    """
    Show the add and modify menu and run the chosen option
    :return: None
    """
    print("\n1. Add a new concert")
    print("2. Modify the information of an existing performer")
    inmenuopt = input("Choose option: ").strip().upper()
    if inmenuopt == '1':
        opt1_main.opt1_1(concerts)
    elif inmenuopt == '2':
        opt1_main.opt1_2(concerts)
    else:
        print("Invalid option. Please try again.")


def opt2():
    """
    Show the remove menu and run the chosen option
    :return: None
    """
    print("\n1. Delete all concerts for an artist")
    print("2. Delete all concerts with ticket prices in a given interval")
    print("3. Delete all concerts taking place in a given interval")
    inmenuopt = input("Choose option: ").strip().upper()
    if inmenuopt == '1':
        opt2_main.opt2_1(concerts)
    elif inmenuopt == '2':
        opt2_main.opt2_2(concerts)
    elif inmenuopt == '3':
        opt2_main.opt2_3(concerts)
    else:
        print("Invalid option. Please try again.")


def opt3():
    """
    Show the display menu and run the chosen option
    :return: None
    """
    print("\n1. Print all concerts from a given city")
    print("2. Print all concerts from an artist taking place in a given city")
    print("3. Print all concerts from an artist with ticket prices lower than a given price")
    inmenuopt = input("Choose option: ").strip().upper()
    if inmenuopt == '1':
        opt3_main.opt3_1(concerts)
    elif inmenuopt == '2':
        opt3_main.opt3_2(concerts)
    elif inmenuopt == '3':
        opt3_main.opt3_3(concerts)
    else:
        print("Invalid option. Please try again.")


def opt4():
    """
    Show the reports menu and run the chosen option
    :return: None
    """
    print("\n1. Print the average ticket price for an artist")
    print("Print the number of concerts per city")
    print("Print the concerts in a given interval, sorted in ascending order by ticket price")
    print("Print the concerts from a given interval which take place in a given city")
    inmenuopt = input("Choose option: ").strip().upper()
    if inmenuopt == '1':
        opt4_main.opt4_1(concerts)
    elif inmenuopt == '2':
        opt4_main.opt4_2(concerts)
    elif inmenuopt == '3':
        opt4_main.opt4_3(concerts)
    elif inmenuopt == '4':
        opt4_main.opt4_4(concerts)
    else:
        print("Invalid option. Please try again.")


def opt5():
    """
    Show the filter menu and run the chosen option
    :return: None
    """
    print(
        "\n1. Eliminate concerts by artists in a user-given list for which ticket prices are greater than a given price")
    print("Eliminate concerts for which the ticket price exceeds a given value or the date is after a given date")
    inmenuopt = input("Choose option: ").strip().upper()
    if inmenuopt == '1':
        opt5_main.opt5_1(concerts)
    elif inmenuopt == '2':
        opt5_main.opt5_2(concerts)
    else:
        print("Invalid option. Please try again.")


def opt6():
    """
    Ask for confirmation and undo the last modification
    :return: None
    """
    print("\nAre you sure you want to undo last modification?")
    inmenuopt = input("Choose option: ").strip().upper()
    if inmenuopt == 'Y':
        opt6_main.opt6(concerts)
    else:
        print("Undo operation canceled.")


def main():
    """
    Run the main menu until the user chooses to exit
    :return: None
    """
    while True:
        print("\n1. Add and modify concerts")
        print("2. Remove concerts")
        print("3. Display the concerts that meet certain criteria")
        print("4. Reports")
        print("5. Filter concerts")
        print("6. Undo last action")
        print("E. Exit")

        opt = input("Choose option: ").strip().upper()

        if opt == 'E':
            break
        elif opt == '1':
            opt1()
        elif opt == '2':
            opt2()
        elif opt == '3':
            opt3()
        elif opt == '4':
            opt4()
        elif opt == '5':
            opt5()
        elif opt == '6':
            opt6()
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
