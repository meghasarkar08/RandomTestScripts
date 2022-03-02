import re
"""Addressline
An address provider returns addresses only with concatenated street names and numbers. Our own system on the other hand has separate fields for street name and street number.

Input: string of address

Output: string of street and string of street-number as JSON object

CASE 2: Consider more complicated cases
"Am Bächle 23" -> {"street": "Am Bächle", "housenumber": "23"}
"Auf der Vogelwiese 23 b" -> {"street": "Auf der Vogelwiese", "housenumber": "23 b"}

CASE 3: Consider other countries (complex cases)
"4, rue de la revolution" -> {"street": "rue de la revolution", "housenumber": "4"}
"200 Broadway Av" -> {"street": "Broadway Av", "housenumber": "200"}
"Calle Aduana, 29" -> {"street": "Calle Aduana", "housenumber": "29"}
"Calle 39 No 1540" -> {"street": "Calle 39", "housenumber": "No 1540"}"""

#Regex pattern to match the preceeding Housenumber values along with the streetname
masks = [r"(?P<name>^\D+) (?P<number>.*)",
         r"(?P<number>^\d+) (?P<name>.*)",
         r"(?P<name>^.*) (?P<number>No.*)"]


def format_address(address_string):
    # Declare variables
    streetName =""
    houseNumber =""
    splitJson = {}

    splitAddress = [None, None]
    add = address_string.replace(',', '')

    for mask in masks:
        m = re.search(mask, add)
        try:
            splitAddress = [m.group('name'), m.group('number')]
        except AttributeError:
            continue

    splitJson['street'] = splitAddress[0]
    splitJson['house number'] = splitAddress[1]

    return print(splitJson)

if __name__ == '__main__':
    addressTest = ['Am Bächle 23', 'Auf der Vogelwiese 23 b', '4, rue de la revolution', '200 Broadway Av',
                   'Calle Aduana, 29', 'Calle 39 No 1540']
    for addressString in addressTest:
        format_address(addressString)