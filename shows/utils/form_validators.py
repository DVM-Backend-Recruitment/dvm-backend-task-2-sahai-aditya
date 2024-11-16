from datetime import datetime


def check_time_format(time):
    """
    returns True if format is valid, returns False if invalid
    """
    try:
        time = datetime.strptime(time, "%Y-%m-%d %H:%M")

    except ValueError:
        return False

    return True