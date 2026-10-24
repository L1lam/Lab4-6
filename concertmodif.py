def add_concert(concerts, artist, city, date, price):
    new_id = len(concerts) + 1
    concerts[new_id] = {
        "artist": artist,
        "city": city,
        "date": date,
        "price": price
    }


def modify_concert_date(concerts, concert_id, new_date):
    concerts[concert_id]["date"] = new_date


def modify_concert_price(concerts, concert_id, new_price):
    concerts[concert_id]["price"] = new_price


def remove_by_artist(concerts, artist):
    remaining = []
    for c in concerts.values():
        current_artist = c["artist"].strip().lower()
        if current_artist != artist:
            remaining.append(c)
    rem_cnt = len(concerts) - len(remaining)

    if rem_cnt == 0:
        print("No concerts found for this artist.\n")
    else:
        concerts.clear()
        new_id = 1
        for concert in remaining:
            concerts[new_id] = concert
            new_id += 1
        print(f"Successfully deleted {rem_cnt} concert(s)!\n")


def remove_by_price(concerts, min_price, max_price):
    remaining = []
    for c in concerts.values():
        current_price = c["price"]
        if not (min_price <= current_price <= max_price):
            remaining.append(c)
    rem_cnt = len(concerts) - len(remaining)

    if rem_cnt == 0:
        print("No concerts found in this price interval.\n")
    else:
        concerts.clear()
        new_id = 1
        for concert in remaining:
            concerts[new_id] = concert
            new_id += 1
        print(f"Successfully deleted {rem_cnt} concert(s)!\n")


def remove_by_date(concerts, start_tuple, end_tuple):
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
        concerts.clear()
        for i in range(len(remaining)):
            new_id = i + 1
            concert = remaining[i]
            concerts[new_id] = concert
        print(f"Successfully deleted {rem_cnt} concert(s)!\n")
