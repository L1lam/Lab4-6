import printers


def opt3_1(concerts):
    """
    Read a city and print all concerts from that city
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    city = input("Enter city: ").strip().upper()
    printers.print_c_from_city(concerts, city)


def opt3_2(concerts):
    """
    Read an artist and a city and print that artist's concerts from that city
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    artist = input("Enter artist: ").strip().upper()
    city = input("Enter city: ").strip().upper()
    printers.print_c_from_artist_within_city(concerts, artist, city)


def opt3_3(concerts):
    """
    Read an artist and a price and print that artist's concerts cheaper than the price
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    artist = input("Enter artist: ").strip().upper()
    price = float(input("Enter price: "))
    printers.print_c_from_artist_within_price(concerts, artist, price)
