import opt2_extras
import opt6_main
import validators
import concertmodif
import printers

concerts = {}


def validators_tests():
    """
    Test that datevalid rejects an impossible month
    :return: None
    """
    assert not validators.datevalid(2026, 13, 1)


def concertmodif_tests():
    """
    Test adding, modifying, removing and undoing concerts, then run the printing functions
    :return: None
    """
    concertmodif.add_concert(concerts, "Artist", "City", "01.01.2023", 50)
    concertmodif.modify_concert_date(concerts, 1, "01.02.2000")
    concertmodif.modify_concert_price(concerts, 1, 100)

    assert concerts[1]["date"] == "01.02.2000"
    assert concerts[1]["price"] == 100

    opt6_main.opt6(concerts)
    assert concerts[1]["price"] == 50
    assert concerts[1]["date"] == "01.02.2000"

    opt6_main.opt6(concerts)
    assert concerts[1]["date"] == "01.01.2023"

    concertmodif.remove_by_artist(concerts, "artist")
    assert concerts == {}

    opt6_main.opt6(concerts)
    assert len(concerts) == 1
    assert concerts[1]["artist"] == "Artist"

    concertmodif.remove_by_artist(concerts, "artist")
    assert concerts == {}

    concertmodif.add_concert(concerts, "Artist", "City", "01.01.2023", 50)
    concertmodif.remove_by_price(concerts, 50, 100)
    assert concerts == {}

    concertmodif.add_concert(concerts, "Artist", "City", "01.01.2023", 50)
    concertmodif.remove_by_date(concerts, (2000, 2, 1), (2024, 2, 1))
    assert concerts == {}

    concertmodif.add_concert(concerts, "Artist", "City", "01.01.2023", 100)
    concertmodif.remove_by_artists_and_price(concerts, ["artist"], 50)
    assert concerts == {}

    concertmodif.add_concert(concerts, "Artist", "City", "01.01.2023", 100)
    concertmodif.remove_by_price_or_date(concerts, 50, (2024, 1, 1))
    assert concerts == {}

    concertmodif.add_concert(concerts, "Artist", "City", "01.01.2023", 50)
    concertmodif.remove_by_price_or_date(concerts, 100, (2022, 1, 1))
    assert concerts == {}

    opt6_main.opt6(concerts)
    assert len(concerts) == 1
    assert concerts[1]["price"] == 50

    opt6_main.opt6(concerts)
    assert concerts == {}

    concertmodif.add_concert(concerts, "Artist", "City", "01.01.2023", 50)

    printers.print_c_from_city(concerts, "CITY")
    printers.print_c_from_artist_within_city(concerts, "ARTIST", "CITY")
    printers.print_c_from_artist_within_price(concerts, "ARTIST", 100.0)
    printers.print_avg_price_for_artist(concerts, "artist")
    printers.print_concerts_per_city(concerts)
    printers.print_c_in_interval_sorted_by_price(concerts, (2020, 1, 1), (2025, 1, 1))
    printers.print_c_in_interval_and_city(concerts, (2020, 1, 1), (2025, 1, 1), "CITY")
    opt2_extras.print_artists(concerts)
    opt2_extras.print_prices(concerts)
    opt2_extras.print_dates(concerts)


if __name__ == "__main__":
    validators_tests()
    concertmodif_tests()
