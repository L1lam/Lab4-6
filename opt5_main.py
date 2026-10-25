import concertmodif


def opt5_1(concerts):
    """
    Eliminate concerts of the given artists with ticket prices above a price
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    if not concerts:
        print("No concerts available.\n")
        return

    artists_input = input("Input artists (separated by comma): ")
    artists = []
    raw_artists = artists_input.split(",")

    for a in raw_artists:
        clean_a = a.strip()
        if clean_a != "":
            artists.append(clean_a.lower())

    max_price = float(input("Input price: "))
    concertmodif.remove_by_artists_and_price(concerts, artists, max_price)


def opt5_2(concerts):
    """
    Eliminate concerts with a ticket price above a price or a date after a date
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    if not concerts:
        print("No concerts available.\n")
        return

    max_price = float(input("Input price: "))
    date_str = input("Input date (e.g: 18.07.2026): ")
    d_tuple = (int(date_str[-4:]), int(date_str[3:5]), int(date_str[:2]))
    concertmodif.remove_by_price_or_date(concerts, max_price, d_tuple)
