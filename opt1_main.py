import validators
import concertmodif


def opt1_1(concerts):
    """
    Read and add one or more concerts, asking again for an invalid date
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    x = int(input("How many concerts would you like to add? "))
    for _ in range(x):
        artist = input("Input artist/band name: ")
        city = input("Input city: ")
        date = input("Input concert date (e.g:01.02.2000): ")
        an = int(date[-4:])
        luna = int(date[3:5])
        zi = int(date[:2])
        while not validators.datevalid(an, luna, zi):
            print("Invalid date. Please try again.")
            date = input("Input concert date (e.g:01.02.2000): ")
            an = int(date[-4:])
            luna = int(date[3:5])
            zi = int(date[:2])
        price = int(input("Input ticket price: "))
        concertmodif.add_concert(concerts, artist, city, date, price)
        print("Concert added successfully!\n")


def opt1_2(concerts):
    """
    Let the user choose a concert and modify its date or its price
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    if not concerts:
        print("No concerts available to modify.\n")
        return

    print("What concert information would you like to modify?\n")
    for concert_id, concert in concerts.items():
        print(f"{concert_id}. {concert['artist']}")

    x = int(input())
    while x < 1 or x > len(concerts):
        print("Invalid option. Please try again.")
        x = int(input())

    print("Would you like to modify the date? (Y/N)")
    conf = input().strip().upper()
    if conf == 'Y':
        new_date = input("Input new concert date (e.g:01.02.2000): ")
        an = int(new_date[-4:])
        luna = int(new_date[3:5])
        zi = int(new_date[:2])
        while not validators.datevalid(an, luna, zi):
            print("Invalid date. Please try again.")
            new_date = input("Input new concert date (e.g:01.02.2000): ")
            an = int(new_date[-4:])
            luna = int(new_date[3:5])
            zi = int(new_date[:2])
        concertmodif.modify_concert_date(concerts, x, new_date)
        print("Date modified successfully!")
    elif conf == 'N':
        pass
    else:
        print("Invalid option.")

    print("Would you like to modify the ticket price? (Y/N)")
    conf = input().strip().upper()
    if conf == 'Y':
        new_price = int(input("Input new ticket price: "))
        concertmodif.modify_concert_price(concerts, x, new_price)
        print("Price modified successfully!")
    elif conf == 'N':
        pass
    else:
        print("Invalid option.")
