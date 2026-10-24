def opt3_1(concerts):
    city = input("Enter city: ").strip().upper()
    print("\nConcerts from city", city, ":")
    for concert in concerts.values():
        if concert["city"].strip().upper() == city:
            print(concert)

def opt3_2(concerts):
    artist = input("Enter artist: ").strip().upper()
    city = input("Enter city: ").strip().upper()
    print("\nConcerts from artist", artist, "in city", city, ":")
    for concert in concerts.values():
        if concert["artist"].strip().upper() == artist and concert["city"].strip().upper() == city:
            print(concert)

def opt3_3(concerts):
    artist = input("Enter artist: ").strip().upper()
    price = float(input("Enter price: "))
    print("\nConcerts from artist", artist, "with ticket prices lower than", price, ":")
    for concert in concerts.values():
        if concert["artist"].strip().upper() == artist and concert["price"] < price:
            print(concert)