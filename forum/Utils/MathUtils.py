# Math Functions and Date Utils

from datetime import date


def GetAge(birth):
    aux = birth.split('-')

    born_year = int(aux[0])
    born_month = int(aux[1])
    born_day = int(aux[2])

    today = date.today()

    return today.year - born_year - ((today.month, today.day) < (born_month, born_day))
