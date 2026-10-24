def print_c_from_city(concerts, city):
    """
    Print all concerts from a given city
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :param city: city to print the concerts of, in upper case
    :type city: str
    :return: None
    """
    print("\nConcerts from city", city, ":")
    for concert in concerts.values():
        if concert["city"].strip().upper() == city:
            print(concert)


def print_c_from_artist_within_city(concerts, artist, city):
    """
    Print all concerts of an artist taking place in a given city
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :param artist: artist to print the concerts of, in upper case
    :type artist: str
    :param city: city to print the concerts of, in upper case
    :type city: str
    :return: None
    """
    print("\nConcerts from artist", artist, "in city", city, ":")
    for concert in concerts.values():
        if concert["artist"].strip().upper() == artist and concert["city"].strip().upper() == city:
            print(concert)


def print_c_from_artist_within_price(concerts, artist, price):
    """
    Print all concerts of an artist with ticket prices lower than a given price
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :param artist: artist to print the concerts of, in upper case
    :type artist: str
    :param price: concerts cheaper than this price are printed
    :type price: float
    :return: None
    """
    print("\nConcerts from artist", artist, "with ticket prices lower than", price, ":")
    for concert in concerts.values():
        if concert["artist"].strip().upper() == artist and concert["price"] < price:
            print(concert)