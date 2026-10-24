def print_artists(concerts):
    """
    Print the list of artists or bands that have at least one concert
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    artists = set()  # Sets prevent duplicates
    for c in concerts.values():
        artists.add(c["artist"])

    print("Available artists:")
    for artist in artists:
        print(artist)


def print_prices(concerts):
    """
    Print the lowest and highest ticket price and ask for the price range to remove
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    prices = [c["price"] for c in concerts.values()]
    min_price_val = min(prices)
    max_price_val = max(prices)

    print(
        f"Ticket prices start at: {min_price_val}, and end at: {max_price_val}. What price range would you like to remove?")


def print_dates(concerts):
    """
    Print the earliest and latest concert date and ask for the date interval to remove
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    date_tuples = []
    for c in concerts.values():
        d = c["date"]
        date_tuples.append((int(d[-4:]), int(d[3:5]), int(d[:2]), d))  # y, m, d, date_str

    date_tuples.sort()
    min_date_str = date_tuples[0][3]
    max_date_str = date_tuples[-1][3]

    print(
        f"Concert dates start at: {min_date_str}, and end at: {max_date_str}. What date interval would you like to remove?")
