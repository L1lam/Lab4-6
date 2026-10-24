import validators
import concertmodif

concerts = {}


def validators_tests():
    try:
        validators.datevalid(2026, 13, 1)
    except AssertionError:
        print("Date not valid")


def concertmodif_tests():
    concertmodif.add_concert(concerts, "Artist", "City", "2023-01-01", 50)
    concertmodif.modify_concert_date(concerts, 1, "01.02.2000")
    concertmodif.modify_concert_price(concerts, 1, 100)
    assert concerts[1]["date"] == "01.02.2000"
    assert concerts[1]["price"] == 100
    concertmodif.remove_by_artist(concerts, "Artist")
    assert concerts == {}
    concertmodif.add_concert(concerts, "Artist", "City", "2023-01-01", 50)
    concertmodif.remove_by_price(concerts, 50, 100)
    assert concerts == {}
    concertmodif.add_concert(concerts, "Artist", "City", "2023-01-01", 50)
    concertmodif.remove_by_date(concerts, "01.02.2000")
