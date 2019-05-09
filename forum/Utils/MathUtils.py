# Math Functions and Date Utils

from datetime import date


def GetAge(birth):
    aux = birth.split('/')

    born_year = aux[2]
    born_month = aux[1]
    born_day = aux[0]

    today = date.today()

    return today.year - born_year - ((today.month, today.day) < (born_month, born_day))
