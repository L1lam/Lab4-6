history = []


def save_state(concerts):
    """
    Save a copy of the current concert dictionary to the undo history
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    state_copy = {}
    for concert_id, concert in concerts.items():
        state_copy[concert_id] = concert.copy()
    history.append(state_copy)


def undo(concerts):
    """
    Revert the concert dictionary to its state before the last modifying operation
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    if not history:
        print("No operations to undo.\n")
        return

    previous_state = history.pop()
    concerts.clear()
    for concert_id, concert in previous_state.items():
        concerts[concert_id] = concert
    print("Undo operation successful!\n")


def add_concert(concerts, artist, city, date, price):
    """
    Add a new concert to the concert dictionary
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :param artist: name of the artist or band
    :type artist: str
    :param city: city where the concert takes place
    :type city: str
    :param date: concert date, in the form dd.mm.yyyy
    :type date: str
    :param price: ticket price
    :type price: float
    :return: None
    """
    save_state(concerts)
    new_id = len(concerts) + 1
    concerts[new_id] = {
        "artist": artist,
        "city": city,
        "date": date,
        "price": price
    }


def modify_concert_date(concerts, concert_id, new_date, save=True):
    """
    Change the date of an existing concert
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :param concert_id: id of the concert to change
    :type concert_id: int
    :param new_date: the new concert date, in the form dd.mm.yyyy
    :type new_date: str
    :param save: whether to save the current state to undo history
    :type save: bool
    """
    if save:
        save_state(concerts)
    concerts[concert_id]["date"] = new_date


def modify_concert_price(concerts, concert_id, new_price, save=True):
    """
    Change the ticket price of an existing concert
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :param concert_id: id of the concert to change
    :type concert_id: int
    :param new_price: the new ticket price
    :type new_price: float
    :param save: whether to save the current state to undo history
    :type save: bool
    """
    if save:
        save_state(concerts)
    concerts[concert_id]["price"] = new_price


def remove_by_artist(concerts, artist):
    """
    Delete every concert of a given artist and renumber the rest
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :param artist: artist name to delete, in lower case
    :type artist: str
    :return: None
    """
    remaining = []
    for c in concerts.values():
        current_artist = c["artist"].strip().lower()
        if current_artist != artist:
            remaining.append(c)
    rem_cnt = len(concerts) - len(remaining)

    if rem_cnt == 0:
        print("No concerts found for this artist.\n")
    else:
        save_state(concerts)
        concerts.clear()
        new_id = 1
        for concert in remaining:
            concerts[new_id] = concert
            new_id += 1
        print(f"Successfully deleted {rem_cnt} concert(s)!\n")


def remove_by_price(concerts, min_price, max_price):
    """
    Delete every concert whose ticket price is in a given interval and renumber the rest
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :param min_price: lowest price of the interval, included
    :type min_price: int
    :param max_price: highest price of the interval, included
    :type max_price: int
    :return: None
    """
    remaining = []
    for c in concerts.values():
        current_price = c["price"]
        if not (min_price <= current_price <= max_price):
            remaining.append(c)
    rem_cnt = len(concerts) - len(remaining)

    if rem_cnt == 0:
        print("No concerts found in this price interval.\n")
    else:
        save_state(concerts)
        concerts.clear()
        new_id = 1
        for concert in remaining:
            concerts[new_id] = concert
            new_id += 1
        print(f"Successfully deleted {rem_cnt} concert(s)!\n")


def remove_by_date(concerts, start_tuple, end_tuple):
    """
    Delete every concert whose date is in a given interval and renumber the rest
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :param start_tuple: start of the interval, as (year, month, day)
    :type start_tuple: tuple
    :param end_tuple: end of the interval, as (year, month, day)
    :type end_tuple: tuple
    :return: None
    """
    remaining = []
    for c in concerts.values():
        c_date = c["date"]
        c_an = int(c_date[-4:])
        c_luna = int(c_date[3:5])
        c_zi = int(c_date[:2])
        c_tuple = (c_an, c_luna, c_zi)

        if not (start_tuple <= c_tuple <= end_tuple):
            remaining.append(c)

    rem_cnt = len(concerts) - len(remaining)

    if rem_cnt == 0:
        print("No concerts found in this date interval.\n")
    else:
        save_state(concerts)
        concerts.clear()
        for i in range(len(remaining)):
            new_id = i + 1
            concert = remaining[i]
            concerts[new_id] = concert
        print(f"Successfully deleted {rem_cnt} concert(s)!\n")


def remove_by_artists_and_price(concerts, artists, max_price):
    """
    Delete every concert of the given artists with a ticket price above a given price and renumber the rest
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :param artists: list of artist names in lower case
    :type artists: list
    :param max_price: maximum price allowed for the given artists
    :type max_price: float
    :return: None
    """
    remaining = []
    for c in concerts.values():
        current_artist = c["artist"].strip().lower()
        current_price = c["price"]
        if not (current_artist in artists and current_price > max_price):
            remaining.append(c)

    rem_cnt = len(concerts) - len(remaining)

    if rem_cnt == 0:
        print("No concerts found matching the criteria.\n")
    else:
        save_state(concerts)
        concerts.clear()
        new_id = 1
        for concert in remaining:
            concerts[new_id] = concert
            new_id += 1
        print(f"Successfully deleted {rem_cnt} concert(s)!\n")


def remove_by_price_or_date(concerts, max_price, date_tuple):
    """
    Delete every concert whose ticket price exceeds max_price or whose date is after date_tuple and renumber the rest
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :param max_price: maximum ticket price allowed
    :type max_price: float
    :param date_tuple: cutoff date as (year, month, day)
    :type date_tuple: tuple
    :return: None
    """
    remaining = []
    for c in concerts.values():
        current_price = c["price"]
        c_date = c["date"]
        c_tuple = (int(c_date[-4:]), int(c_date[3:5]), int(c_date[:2]))
        if not (current_price > max_price or c_tuple > date_tuple):
            remaining.append(c)

    rem_cnt = len(concerts) - len(remaining)

    if rem_cnt == 0:
        print("No concerts found matching the criteria.\n")
    else:
        save_state(concerts)
        concerts.clear()
        new_id = 1
        for concert in remaining:
            concerts[new_id] = concert
            new_id += 1
        print(f"Successfully deleted {rem_cnt} concert(s)!\n")
