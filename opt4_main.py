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
    total_price = 0
    count = 0

    for c in concerts.values():
        if c["artist"].strip().lower() == artist:
            total_price += c["price"]
            count += 1

    if count == 0:
        print("No concerts found for this artist.\n")
    else:
        print(f"Average ticket price for {artist.title()}: {total_price / count:.2f}\n")  #:.2f pentru 2 zecimale


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
