import opt2_extras
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
    Test adding, modifying and removing concerts, then run the printing functions
    :return: None
    """
    concertmodif.add_concert(concerts, "Artist", "City", "01.01.2023", 50)
    concertmodif.modify_concert_date(concerts, 1, "01.02.2000")
    concertmodif.modify_concert_price(concerts, 1, 100)

    assert concerts[1]["date"] == "01.02.2000"
    assert concerts[1]["price"] == 100

    concertmodif.remove_by_artist(concerts, "artist")
    assert concerts == {}

    concertmodif.add_concert(concerts, "Artist", "City", "01.01.2023", 50)
    concertmodif.remove_by_price(concerts, 50, 100)
    assert concerts == {}

    concertmodif.add_concert(concerts, "Artist", "City", "01.01.2023", 50)
    concertmodif.remove_by_date(concerts, (2000, 2, 1), (2024, 2, 1))
    assert concerts == {}

    concertmodif.add_concert(concerts, "Artist", "City", "01.01.2023", 50)

    printers.print_c_from_city(concerts, "CITY")
    printers.print_c_from_artist_within_city(concerts, "ARTIST", "CITY")
    printers.print_c_from_artist_within_price(concerts, "ARTIST", 100.0)
    opt2_extras.print_artists(concerts)
    opt2_extras.print_prices(concerts)
    opt2_extras.print_dates(concerts)
