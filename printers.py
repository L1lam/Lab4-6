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


def print_avg_price_for_artist(concerts, artist):
    """
    Print the average ticket price of a given artist or band
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :param artist: artist name in lower case
    :type artist: str
    :return: None
    """
    total_price = 0
    count = 0

    for c in concerts.values():
        if c["artist"].strip().lower() == artist:
            total_price += c["price"]
            count += 1

    if count == 0:
        print("No concerts found for this artist.\n")
    else:
        print(f"Average ticket price for {artist.title()}: {total_price / count:.2f}\n")


def print_concerts_per_city(concerts):
    """
    Print how many concerts take place in each city
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    city_counts = {}
    for c in concerts.values():
        city = c["city"].strip().upper()

        if city in city_counts:
            city_counts[city] += 1
        else:
            city_counts[city] = 1

    for city, count in city_counts.items():
        print(f"{city}: {count} concert(s)")
    print()


def print_c_in_interval_sorted_by_price(concerts, s_tuple, e_tuple):
    """
    Print the concerts inside a date interval, ordered by ticket price
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :param s_tuple: start of the interval, as (year, month, day)
    :type s_tuple: tuple
    :param e_tuple: end of the interval, as (year, month, day)
    :type e_tuple: tuple
    :return: None
    """
    filtered = []
    for c in concerts.values():
        c_date = c["date"]
        c_tuple = (int(c_date[-4:]), int(c_date[3:5]), int(c_date[:2]))
        if s_tuple <= c_tuple <= e_tuple:
            filtered.append(c)

    n = len(filtered)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if filtered[j]["price"] > filtered[j + 1]["price"]:
                temp = filtered[j]
                filtered[j] = filtered[j + 1]
                filtered[j + 1] = temp

    if not filtered:
        print("No concerts found in this interval.\n")
    else:
        for c in filtered:
            print(c)
        print()


def print_c_in_interval_and_city(concerts, s_tuple, e_tuple, city):
    """
    Print the concerts of one city inside a date interval
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :param s_tuple: start of the interval, as (year, month, day)
    :type s_tuple: tuple
    :param e_tuple: end of the interval, as (year, month, day)
    :type e_tuple: tuple
    :param city: city in upper case
    :type city: str
    :return: None
    """
    filtered = []
    for c in concerts.values():
        c_date = c["date"]
        c_tuple = (int(c_date[-4:]), int(c_date[3:5]), int(c_date[:2]))
        if s_tuple <= c_tuple <= e_tuple and c["city"].strip().upper() == city:
            filtered.append(c)

    if not filtered:
        print("No concerts found in this interval for the given city.\n")
    else:
        for c in filtered:
            print(c)
        print()