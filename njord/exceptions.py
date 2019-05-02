class ConnectionException(Exception):
    pass

class JsonParseException(Exception):
    pass

class InvalidCountryException(Exception):
    def __init__(self, country_codes):
        super(InvalidCountryException, self).__init__()
        self.msg = "Invalid country code, available country codes:\n{}".format(", ".join(map(str, country_codes)))

    def __str__(self):
        return self.msg

class InvalidContinentException(Exception):
    def __init__(self, continents):
        super(InvalidContinentException, self).__init__()
        self.msg = "Invalid continent, available continents:\n{}".format(", ".join(map(str, continents)))

    def __str__(self):
        return self.msg
