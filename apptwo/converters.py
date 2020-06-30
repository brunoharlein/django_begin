class TwoDigitDayConverter:
    # création d'une classe TwoDigitDayConverter

    regex = '[0-9]{2}'
    # création d'une petite regex : nous voulons des chiffres en 0 et 9 et nous en voulons 2

    def to_python(self, value):
        return int(value)
        # nous retournons un integer

    def to_url(self, value):
        return '%02d' % value
        # Nous retournons une valeur de 2 chiffres
