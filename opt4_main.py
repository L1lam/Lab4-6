import printers


def opt4_1(concerts):
    """
    Print the average ticket price of a given artist or band
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    if not concerts:
        print("No concerts available.\n")
        return

    artist = input("Enter artist: ").strip().lower()
    printers.print_avg_price_for_artist(concerts, artist)


def opt4_2(concerts):
    """
    Print how many concerts take place in each city
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    if not concerts:
        print("No concerts available.\n")
        return

    printers.print_concerts_per_city(concerts)


def opt4_3(concerts):
    """
    Print the concerts inside a date interval, ordered by ticket price
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    if not concerts:
        print("No concerts available.\n")
        return

    start_str = input("Input start date (e.g: 11.09.2026): ")
    end_str = input("Input end date (e.g: 13.09.2026): ")

    s_tuple = (int(start_str[-4:]), int(start_str[3:5]), int(start_str[:2]))
    e_tuple = (int(end_str[-4:]), int(end_str[3:5]), int(end_str[:2]))

    printers.print_c_in_interval_sorted_by_price(concerts, s_tuple, e_tuple)


def opt4_4(concerts):
    """
    Print the concerts of one city inside a date interval
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    if not concerts:
        print("No concerts available.\n")
        return

    start_str = input("Input start date (e.g: 11.09.2026): ")
    end_str = input("Input end date (e.g: 13.09.2026): ")
    city = input("Enter city: ").strip().upper()

    s_tuple = (int(start_str[-4:]), int(start_str[3:5]), int(start_str[:2]))
    e_tuple = (int(end_str[-4:]), int(end_str[3:5]), int(end_str[:2]))

    printers.print_c_in_interval_and_city(concerts, s_tuple, e_tuple, city)
