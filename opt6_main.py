import concertmodif


def opt6(concerts):
    """
    Undo the last modification of the concert list
    :param concerts: dictionary of concerts, keyed by id
    :type concerts: dict
    :return: None
    """
    concertmodif.undo(concerts)
