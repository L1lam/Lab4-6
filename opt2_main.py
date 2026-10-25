import concertmodif
import opt2_extras


def opt2_1(concerts):
    """
    Remove every concert of an artist or band chosen by the user
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    if not concerts:
        print("No concerts available to remove.\n")
        return

    opt2_extras.print_artists(concerts)

    artist = input("Input artist/band name to remove: ").strip().lower()
    concertmodif.remove_by_artist(concerts, artist)


def opt2_2(concerts):
    """
    Remove the concerts whose ticket price is inside a range given by the user
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    if not concerts:
        print("No concerts available to remove.\n")
        return

    opt2_extras.print_prices(concerts)

    min_price = float(input("Input minimum price: "))
    max_price = float(input("Input maximum price: "))
    concertmodif.remove_by_price(concerts, min_price, max_price)


def opt2_3(concerts):
    """
    Remove the concerts whose date is inside an interval given by the user
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    if not concerts:
        print("No concerts available to remove.\n")
        return

    opt2_extras.print_dates(concerts)

    start_str = input("Input start date (e.g: 11.09.2026): ")
    end_str = input("Input end date (e.g: 13.09.2026): ")

    s_an = int(start_str[-4:])
    s_luna = int(start_str[3:5])
    s_zi = int(start_str[:2])
    start_tuple = (s_an, s_luna, s_zi)

    e_an = int(end_str[-4:])
    e_luna = int(end_str[3:5])
    e_zi = int(end_str[:2])
    end_tuple = (e_an, e_luna, e_zi)

    concertmodif.remove_by_date(concerts, start_tuple, end_tuple)
