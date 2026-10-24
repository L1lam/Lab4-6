def datevalid(an, luna, zi):
    """
    Check whether a date is a real day of the calendar
    :param an: the year
    :type an: int
    :param luna: the month, from 1 to 12
    :type luna: int
    :param zi: the day of the month
    :type zi: int
    :return: True if the date is valid, False otherwise
    :rtype: bool
    """
    este_bisect = (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0)

    if an > 0 and 1 <= luna <= 12:
        if luna in (1, 3, 5, 7, 8, 10, 12) and 1 <= zi <= 31:
            este_valid = True
        elif luna in (4, 6, 9, 11) and 1 <= zi <= 30:
            este_valid = True
        elif luna == 2 and ((este_bisect and 1 <= zi <= 29) or (not este_bisect and 1 <= zi <= 28)):
            este_valid = True
        else:
            este_valid = False
    else:
        este_valid = False
    return este_valid
